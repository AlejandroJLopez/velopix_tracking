import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ht_solver import *
from ht_solver_4 import ht_solver
from classical_solver import classical_solver
import event_model as em
import ht_pruebas as htp
import math as m
import validator_lite as vl


class Test:
	"""Clase genérica para representar los diferentes tests del proyecto
	"""

	def __init__(self, plot = False):
		self.plot = plot

	def get_events(self, j= 0, n = 20):
		events = []
		for i in range(j,n):
			f = open("../../velojson_5k/"+str(i)+".json")
			json_data = json.loads(f.read())
			events.append(em.event(json_data))
			f.close()
		return events

	def run(self):
		pass
	def graphs(self):
		pass