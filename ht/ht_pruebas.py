from ht_solver import *
import event_model as em
import math as m
import cmath as cm
from ht_aux import hit_ht

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import validator_lite as vl


def prueba_1(n = 5000, eta = 6, bins = 100):
	"""
	recorrido de los 5k archivos para determinar la distribucion de theta
	"""
	j = 0

	bin_edges = np.linspace(start = -eta, stop = eta, num = bins+1)
	hist = np.zeros(bins)

	#hist = histogram_n([], -eta*bins, eta*bins, bins)

	for i in range(j,n):

		#open file
		f = open("velojson_5k/"+str(i)+".json")
		json_data = json.loads(f.read())
		event = em.event(json_data)
		f.close()

		hit_ps = []

		for h in event.hits:
			theta = cm.phase(hit_ht(h).complex_ht)
			pseudorapidity = -m.log(m.tan(theta/2))

			hit_ps.append(pseudorapidity)

		hist += np.histogram(hit_ps, bins=bin_edges, density = 1)[0]
		#print(hist)

	# plt.hist(hist , bins = bin_edges, range = (-6, 6))
	# plt.plot(hist)
	# plt.ylabel("n_hits")
	# plt.xlabel("pseudorapidity")
	# plt.show()
	return (hist, bin_edges)

def prueba_2(n = 5000, eta = 6, bins = 100):
	"""
	recorrido de los 5k archivos para determinar la distribucion de theta
	"""
	j = 0

	bin_edges = np.linspace(start = -eta, stop = eta, num = bins+1)
	hist = np.zeros(bins)

	#hist = histogram_n([], -eta*bins, eta*bins, bins)

	for i in range(j,n):

		#open file
		f = open("velojson_5k/"+str(i)+".json")
		json_data = json.loads(f.read())
		event = em.event(json_data)
		f.close()

		hit_ps = []

		for h in event.hits:
			theta = cm.phase(hit_ht(h).complex_ht)
			pseudorapidity = -m.log(m.tan(theta/2))

			hit_ps.append(pseudorapidity)

		hist += np.histogram(hit_ps, bins=bin_edges)[0]
		

	plt.hist(hist , bins = bin_edges, range = (-6, 6))
	plt.plot(hist)
	plt.ylabel("n_hits")
	plt.xlabel("pseudorapidity")
	plt.show()

	

	return (hist, bin_edges)


if __name__ == "__main__":
	prueba_2(n = 100)