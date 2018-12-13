import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from event_model import *
import json
import math as m
import cmath as cm
from ht_aux import *
import matplotlib.pyplot as graph
import copy


class ht_solver:
	def __init__(self, nbins = 32, n_rotations = 500, threshold = 10, max_tolerance = (0.4,0.4), bin_size = 4, vble = 0):
		self.nbins = nbins
		self.n_rotations = n_rotations
		self. threshold = threshold
		self.max_tolerance = max_tolerance
		self.bin_size = bin_size
		self.vble = vble

	def compatible(self, hits):
		return True

	def new_track(self, hits):
		return track(hits)

	def filtra_datos(self, hits, l_hits):
		# for n in range(len(l_hits)):
		# 	longitud = len(l_hits[n])
		# 	print("ANTES: " + str(longitud))
		# 	l_hits[n] = [x for x in l_hits[n] if x not in hits]
		# 	print("DESPUES: " + str(len(l_hits[n])))

	def recta_punto_offset():
 
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

		# NUEVO REGIMEN

		for t in reversed(range(3, self.threshold+1)):
			print("umbral: " + str(t))
			for n in range(self.nbins):

				#reference
				h_bin_rotated = classified_hits[n]
				print("###########")
				print("hits en bin " + str(n)+ ": "+str(len(h_bin_rotated)))


				for k in range(int((self.n_rotations + 1))):

					#rotation angle

					angle = m.fmod((m.pi/self.n_rotations), 2*m.pi)

					#rotate
					(h.c_rotate(angle) for h in h_bin_rotated if h not in used_hits)



					#histogram

					hist = histogram(h_bin_rotated, -50, 750, self.bin_size)

					#tracks

					for n1,b in hist.items():
						if (len(b) >= self.threshold and self.compatible(b)):
							n_track = self.new_track(b)
							tracks.append(n_track)
							used_hits += b
							h_bin_rotated = [x for x in h_bin_rotated if x not in used_hits]
							#self.filtra_datos(b, [classified_hits[n], h_bin_rotated])

				print("tracks encontrados para bin "+ str(n)+ ": " + str(len(tracks)))
				print("hits restantes: " +str(len(h_bin_rotated)))
	

		 			

		return tracks


		#ANTIGUO REGIMEN

		"""
		for n, e in enumerate(classified_hits_cmp):
			hit_nr = list(e)
			hit_rotated = list(hit_nr)

			for k in range(n_rotations+1):

				#180 degrees
				angle = m.fmod((m.pi/n_rotations)*k, 2*m.pi)

				hit_rotated = [rotate(z, angle) for z in hit_nr]

				#graph.plot([angle for _ in hit_rotated], [x.imag for x in hit_rotated], 'ko-', ls = 'none', markersize = 1)

				#graph.hist([x.imag for x in hit_rotated], bins = 40)

				hit_classified = histogram(hit_rotated, -50, 750, bin_size)

				hit_classified = list(filter(lambda xy: xy[0]>= threshold, hit_classified))
				
				if hit_classified:
					#solucion = [x.id for x in classified_hits[n]]
					soluciones.append((hit_classified, angle, solucion))
				



		list(filter(lambda x: len(x[0:-1]) > 9, event.montecarlo['particles']))
		print(soluciones)
		graph.show()

		#encuentra recta candidata


		#una vez encuentra candidata, elimina todos los puntos


				


	

		return soluciones
	"""
