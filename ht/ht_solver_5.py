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

#version de Renato pero con Rho, NumPy sin Theta adaptativo

class accumulator(np.ndarray):
	def __init__(self, thetas, rhos, n_theta_bins, n_rho_bins):
		pass


class ht_solver:
	def __init__(self, theta_max = 90, theta_min = -90, n_phi_bins = 32, n_rho_bins = 100, n_rotations = 360, threshold = 3, max_tolerance = (0.4,0.4)):
		self.theta_max = theta_max
		self.theta_min = theta_min
		self.nbins = n_phi_bins
		self.n_rho_bins = n_rho_bins #no usada en el acumulador, modificar
		self.n_rotations = n_rotations
		self.threshold = threshold
		self.max_tolerance = max_tolerance

	def compatible(self, hits):
		return True

	def new_track(self, hits, total_hits):
		return track(hits)

	def solve(self, event):

		print("HT_solver using theta angle")

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
		rot = cm.rect(1, m.radians(rot_angle))
		
		angles = np.deg2rad(np.arange(self.theta_min, self.theta_max, rot_angle))
		rho = np.arange(-800, 800, 1)


		# print("angulos: ", angles)
		# print("modulos: ", rho)

		#algoritmo
		#for n in range(self.nbins):
		for n in range(12,13):
			h_bin_rotated = np.array([x.complex for x in classified_hits[n]], dtype= complex)
			acc = np.zeros((len(rho), len(angles)+1), dtype=int)
			print(acc.shape)

			#rotar y acumular
			for k in range(self.n_rotations):
				h_bin_rotated *= rot
				x,y = np.array([cm.polar(xi)[0] for xi in h_bin_rotated]), np.array([xi.imag for xi in h_bin_rotated])
				x_index = np.digitize(x, rho)
				y_index = np.digitize(y, angles)
				acc[x_index, y_index] += 1


			#sacar tracks del acumulador

			plt.imshow(acc)
			plt.show()

			if n == 12: 
				np.savetxt("acumulador_"+str(n)+".csv", acc, delimiter=",")
			weak_tracks = (np.argwhere(acc >= self.threshold))

			# for w in weak_tracks:
			# 	r = rho[w[0]]
			# 	a = angles[w[1]]



			print("bin: ", n)

			



		#--------------------------------------

		#algoritmo
		# for n in range(self.nbins):
		# 	h_bin_rotated = list(filter(lambda x: x not in used_hits, classified_hits[n]))
		# 	acc = accumulator(self.theta_max, self.theta_min, self.n_rotations) 

		# 	for k in acc.get_angles():
		# 		#rotar y acumular
		# 		for h in h_bin_rotated:
		# 			h.c_rotate(k)
		# 			acc.inc(h)
		# 	#sacar tracks del acumulador
		# 	weak_tracks = acc.get_tracks(self.threshold)
		# 	#posprocesado
		# 	for a in weak_tracks:
		# 		if not [x for x in a if x in used_hits]:
		# 			tracks.append(track(a))
		# 		used_hits.update(a)

			print("bin: ", n)

		return tracks