import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import event_model as em
import json
from ht_aux import *
import matplotlib.pyplot as plt
import copy
import itertools

class test_1:
	"""Recibé un número de bins, un evento y devuelve cuantos son reconstruibles
	"""
	def __init__(self, min_bins = 12, max_bins = 32):
		self.min_bins = min_bins
		self.max_bins = max_bins

	def run(self, n = 40, plot = True):
		classifiers = list()
		results = dict()
		
		for bin in range(self.min_bins, self.max_bins +1):
			classifiers.append(classifier(bin))
			results[bin] = [0,0,0]

		for i in range(n):
			print("velojson_5k/"+str(i)+".json")
			#abre archivo
			f = open("velojson_5k/"+str(i)+".json")
			json_data = json.loads(f.read())
			event = em.event(json_data)
			f.close()

			for m in range(0, self.max_bins - self.min_bins +1):
				res = classifiers[m].classify(event)
				aux = [x+y for x,y in zip(results[self.min_bins+m], res)]
				results[self.min_bins+m] = aux

		if plot:
			p_results = {k:(v[2]/v[0]) for k,v in results.items()}
			print(p_results)
			#plt.hist(list(p_results.keys()), list(p_results.items()))
			plt.bar(list(p_results.keys()), p_results.values())
			plt.show()

		return results
    	
class classifier:
	def __init__(self, nbins = 32):
		self.nbins = nbins
		self.phi_bin = [((2*m.pi)/self.nbins) * n - m.pi for n in range(self.nbins + 1)]
		self.bins = list(zip(self.phi_bin[:-1], self.phi_bin[1:]))

	def classify(self, event):
		print(self.nbins)
		tracks = list()
		used_hits = list()

		#probando con tracks

		particulas = event.montecarlo['particles']

		for t in particulas:
			hits = [hit_ht(y) for x in t[-1] for y in event.hits if y.id == x]
			tracks.append(hits)

		phi_bin = self.phi_bin
		bins = self.bins

		#comprueba cuantos tracks son partidos por phi bin

		count = 0
		partial = 0
		valid = 0

		for t in tracks:
		 	classified_hits = [[x for x in t if x.phi >= a[0] and x.phi <= a[1]] for a in bins]
		 	beans = [x for x in classified_hits if x != []]
		 	count += 1

		 	if len(beans) == 1:
		 		valid +=1
		 	elif list(filter(lambda x: len(x) >= 3, beans)):
		 		partial += 1

		return (count, partial, valid)