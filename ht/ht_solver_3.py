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

angles = map(lambda x: m.radians(x),list(range(-90,90)))

class ht_solver:
	def __init__(self, theta_max = 90, theta_min = -90, nbins = 32, n_rotations = 300, threshold = 10, max_tolerance = (0.4,0.4), bin_size = 4, vble = 0):
		self.theta_max = theta_max
		self.theta_min = theta_min
		self.nbins = nbins
		self.n_rotations = n_rotations
		self.threshold = threshold
		self.max_tolerance = max_tolerance
		self.bin_size = bin_size
		self.vble = vble

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

		#algoritmo
		for n in range(self.nbins):
			h_bin_rotated = list(filter(lambda x: x not in used_hits, classified_hits[n]))
			acc = accumulator(self.theta_max, self.theta_min, self.n_rotations) 

			for k in acc.get_angles():
				#rotar y acumular
				for h in h_bin_rotated:
					h.c_rotate(k)
					acc.inc(h)
			#sacar tracks del acumulador
			weak_tracks = acc.get_tracks(self.threshold)
			#posprocesado
			for a in weak_tracks:
				if not [x for x in a if x in used_hits]:
					tracks.append(track(a))
				used_hits.update(a)

			#print("bin: ", n)

		return tracks