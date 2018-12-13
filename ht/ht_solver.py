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


class ht_solver:
	def __init__(self, angle_hist = tuple(), nbins = 32, n_rotations = 10000, threshold = 10, max_tolerance = (0.4,0.4), bin_size = 4, vble = 0):
		self.nbins = nbins
		self.n_rotations = n_rotations
		self.threshold = threshold
		self.max_tolerance = max_tolerance
		self.bin_size = bin_size
		self.angle_hist = angle_hist
		self.vble = vble

	def compatible(self, hits):
		return True

	def angle_eta(self, angle_hist, n_rotations):
		return None

	def angle_theta(self, angle_hist, n_rotations):
		h = angle_hist[0]

		pos = filter(lambda x: x >= 0, angle_hist[1])
		neg = filter(lambda x: x < 0, angle_hist[1])

		theta_pos = list(map(lambda x: 2 * m.atan(m.exp(-x)), pos))
		#theta_neg = list(map(lambda x: 2 * m.atan(m.exp(-x)), neg))

		return list([m.pi/300]*300)

	def new_track(self, hits, total_hits):
		t = track([])
		return track(hits)

	def filtra_datos(self, hits, l_hits):
		# for n in range(len(l_hits)):
		# 	longitud = len(l_hits[n])
		# 	print("ANTES: " + str(longitud))
		# 	l_hits[n] = [x for x in l_hits[n] if x not in hits]
		# 	print("DESPUES: " + str(len(l_hits[n])))

		return None

	def hough_transform(self, hits, angle, theta_rotations):
		return None

	def solve(self, event):

		print("HT_solver using theta angle")

		tracks = list()
		used_hits = list()

		hits_ht_total = [hit_ht(x) for x in event.hits]

		#filtra z >= 0
		hits_ht = list(filter(lambda x: x.z >= 0, hits_ht_total))
		hits_ht_n = list(filter(lambda x: x.z < 0, hits_ht_total))



		# Clasifica los hits en phi bins

		phi_bin = [((2*m.pi)/self.nbins) * n - m.pi for n in range(self.nbins + 1)]
		bins = list(zip(phi_bin[:-1], phi_bin[1:]))

		classified_hits = [[x for x in hits_ht if x.phi >= a[0] and x.phi <= a[1]] for a in bins]

		#calcula lista de rotaciones
		angulo = self.angle_theta(self.angle_hist, self.n_rotations)

		# NUEVO REGIMEN

		for t in reversed(range(3, self.threshold+1)):
			#print("umbral: " + str(t))
			for n in range(self.nbins):

				#reference
				h_bin_rotated = classified_hits[n]
				#print("###########")
				#print("hits en bin " + str(n)+ ": "+str(len(h_bin_rotated)))



				#####################
				for k in angulo:
					#rotar
					(h.c_rotate(k) for h in h_bin_rotated if h not in used_hits)
					#histograma
					hist = histogram(h_bin_rotated, -50, 750, self.bin_size)
					print(hist)
					#print(hist)

					tracks
		 			
		return tracks