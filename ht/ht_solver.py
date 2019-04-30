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



angles = ([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
0.0003843431763462092, 0.003288269397628679, 0.008469784812073871,
0.016583696312716067, 0.022106850106135664, 0.02345916868957603,
0.025580173625708816, 0.02923855126722644, 0.0318008391095345,
0.035686975670368395, 0.037921860066159316, 0.0385339621618218,
0.038377377904791864, 0.03907488959519794, 0.04109625000412986,
0.04173682196470687, 0.04535249480885269, 0.04212116514105308,
0.03795032993107385, 0.030163821876948792, 0.022064145308763865,
0.021153109631498777, 0.01961573692611394, 0.017195798408378548,
0.016583696312716067, 0.0151886729319039, 0.015501841445963773,
0.01632746752848526, 0.01742355732769482, 0.01641287712322886,
0.014875504417844024, 0.013736709821262665, 0.011288301438612739,
0.010476910288548521, 0.00899647731299275, 0.007544514202351515,
0.0070320566338899024, 0.0032313296677996114, 0.0, 0.02727413058812359,
0.0264057997082303, 0.0, 0.0034306187222013494, 0.0071459360935480385,
0.007174405958462573, 0.009893278057800572, 0.011089012384211,
0.012825674143997576, 0.014448456444126014, 0.01598582914951085,
0.017879075166327366, 0.02056947740075083, 0.022291904228080136,
0.02461219821861466, 0.02818516626538868, 0.03457665093870157,
0.03994322047509123, 0.04448416392895941, 0.05073329927769962,
0.056854320234324435, 0.066534074305266, 0.07450563648133554,
0.08032772385635774, 0.08903950252020515, 0.08965160461586763,
0.09049146563084638, 0.08980818887289756, 0.09191495887657308,
0.10008581010704434, 0.10263386301689513, 0.11362323087390527,
0.11002179296221672, 0.10568013856275028, 0.0950608789496291,
0.0871177866384741, 0.07675475580958373, 0.06398602139541522,
0.06182231166191062, 0.04687563258178026, 0.04192187608665134,
0.034690530398359704, 0.032156712420966176, 0.024911131800217267,
0.021338163753443246, 0.016811455232032337, 0.010149506842031378,
0.003743787236261224, 0.0005551623658334134, 0.0, 0.0])




class ht_solver:
	def __init__(self, angle_hist = angles, nbins = 32, n_rotations = 10000, threshold = 10, max_tolerance = (0.4,0.4), bin_size = 4, vble = 0):
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
		return track(hits)

	def solve(self, event):

		print("HT_solver using theta angle")

		tracks = list()
		used_hits = list()

		hits_ht_total = [hit_ht(x) for x in event.hits]

		#filtra z >= 0
		#hits_ht = list(filter(lambda x: x.z >= 0, hits_ht_total))
		#hits_ht_n = list(filter(lambda x: x.z < 0, hits_ht_total))

		hits_ht = hits_ht_total

		# Clasifica los hits en phi bins

		phi_bin = [((2*m.pi)/self.nbins) * n - m.pi for n in range(self.nbins + 1)]
		bins = list(zip(phi_bin[:-1], phi_bin[1:]))

		classified_hits = [[x for x in hits_ht if x.phi >= a[0] and x.phi <= a[1]] for a in bins]
		for t in reversed(range(3, self.threshold+1)):
			#print("umbral: " + str(t))
			for n in range(self.nbins):

				#reference
				h_bin_rotated = list(filter(lambda x: x not in used_hits, classified_hits[n]))

				for k in self.angle_hist:
					#rotar
					(h.c_rotate(k) for h in h_bin_rotated)
					#histograma
					hist = histogram(h_bin_rotated, -50, 750, self.bin_size)
					print(hist)
					for k,v in hist.items():
						if (len(v) >= t):
							tracks.append(self.new_track(v, h_bin_rotated))
							h_bin_rotated = list(filter(lambda x: x not in tracks[-1], h_bin_rotated))
							used_hits += v
		 			
		return tracks