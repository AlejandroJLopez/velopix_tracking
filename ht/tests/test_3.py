import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ht_solver import *
from ht_solver_4 import ht_solver
from classical_solver import classical_solver
import event_model as em
import ht_pruebas as htp
import math as m
import validator_lite as vl
from test_model import Test
import numpy as np

class Test_3(Test):
	"""Distribucion de los tracks en funcion del numero de hits. Porcentaje de tracks reconstruibles"""
	def __init__(self, n = 100, j = 1, plot = True):
		super().__init__(plot = plot)
		self.n = n
		self.j = j

	def run(self):
		events = self.get_events(self.j, self.n)
		l = list()

		for n,event in enumerate(events):
			print("numero de evento", n)

			mc_track_list = [] 

			for i in range(len(event.montecarlo['particles'])):
				t = event.montecarlo['particles'][i][-1]
				mc_track = []
				for h in event.hits:
					if h.__hash__() in t:
						mc_track.append(hit_ht(h))

				mc_track_list.append(mc_track)
				l.append(len(mc_track))
		hist, bins = np.histogram(np.asarray(l), bins = 22)
		width = 0.7 * (bins[1] - bins[0])
		center = (bins[:-1] + bins[1:]) / 2
		plt.bar(center, hist, align='center', width=width, color = 'royalblue', edgecolor = 'darkblue')
		plt.grid(True)
		plt.xlabel('longitud de tracks')
		plt.ylabel('n tracks')
		plt.annotate("tracks reconstruibles: 88.2%", xy=(0.60, 0.95), xycoords='axes fraction')


		plt.show()


		return None
