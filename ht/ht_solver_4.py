import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from event_model import *
import json
import math as m
import cmath as cm
from ht_aux import *
import matplotlib.pyplot as graph
import copy
import numpy as np
from matplotlib import pyplot as plt 

#version de Renato pero con Rho, NumPy sin Theta adaptativo LA REQUETEDEFINITIVA

class accumulator(np.ndarray):
	def __init__(self, thetas, rhos, n_theta_bins, n_rho_bins):
		pass

class ht_solver:
	def __init__(self,
		theta_min = -10,
		theta_max = 10,
		n_rotations = 200, 
		rho_min = -100,
		rho_max = 100,
		n_rho_bins = 500, 
		n_phi_bins = 32,
		threshold = 4):
		self.theta_min = theta_min
		self.theta_max = theta_max
		self.n_rotations = n_rotations
		self.rho_min = rho_min
		self.rho_max = rho_max
		self.n_rho_bins = n_rho_bins
		self.nbins = n_phi_bins
		self.threshold = threshold
		self.__max_slopes = (0.7, 0.7)

	def are_compatible(self, hit_0, hit_1):
		hit_distance = abs(hit_1[2] - hit_0[2])
		dxmax = self.__max_slopes[0] * hit_distance
		dymax = self.__max_slopes[1] * hit_distance
		return abs(hit_1[0] - hit_0[0]) < dxmax and \
				abs(hit_1[1] - hit_0[1]) < dymax

	def compatible(self, hits):
		return all([self.are_compatible(x,y) for x,y in list(zip(hits[:-1:], hits[1:]))])

	def new_track(self, hits, total_hits):
		return track(hits)

	def solve(self, event):
		tracks = list()
		used_hits = set()
		hits_ht_total = [hit_ht(x) for x in event.hits]
		hits_ht = hits_ht_total

		# Clasifica los hits en phi bins
		phi_bin = [((2*m.pi)/self.nbins) * n - m.pi for n in range(self.nbins + 1)]
		bins = list(zip(phi_bin[:-1], phi_bin[1:]))
		classified_hits = [[x for x in hits_ht if x.phi >= a[0] and x.phi <= a[1]] for a in bins]

		#crea angulos y valores para el acumulador
		rot_angle = (self.theta_max-self.theta_min)/self.n_rotations
		angles = np.deg2rad(np.arange(self.theta_min, self.theta_max, rot_angle))
		rho = np.arange(self.rho_min, self.rho_max, (self.rho_max - self.rho_min)/self.n_rho_bins)

		#algoritmo
		for n in range(self.nbins):
			acc = np.zeros((len(rho), len(angles)), dtype=int)
			#rotar y acumular
			for h in classified_hits[n]:
				for k in angles:
					v = h.z * m.sin(k) + h.r * m.cos(k)
					x_index = np.digitize(v, rho)
					y_index = np.digitize(k, angles)
					if x_index == len(rho): x_index -= 1
					if y_index == len(angles): y_index -= 1
					acc[x_index, y_index] += 1

			#sacar tracks del acumulador

			kandidaten = np.argwhere(acc>=self.threshold)

			k = list(sorted([(x,y) for x,y in kandidaten], key = lambda xy: acc[xy], reverse = True))

			for x,y in k:
				r = rho[x]
				a = angles[y]
				new_track = list()
				for h in classified_hits[n]:
					v = h.z * m.sin(a) + h.r * m.cos(a)
					if abs(r-v) < 1:
						new_track.append(h)
				if(len(new_track) >3 and all([h1 not in used_hits for h1 in new_track])): #and self.compatible(new_track)
					tracks.append(track(new_track))
					used_hits.update(new_track)

			# plt.imshow(acc, aspect='auto', interpolation = None, extent = [angles[0], angles[-1], rho[0], rho[-1]], vmin = 0, vmax = 10)
			# plt.show()

			print(".", end="", flush= True)

		print("")
		return tracks