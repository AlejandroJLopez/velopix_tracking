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

class Test_2(Test):
	"""Rho y theta de los tracks del Monte Carlo"""
	def __init__(self, n = 100, j = 1, plot = True):
		super().__init__(plot = plot)
		self.n = n
		self.j = j

	def run(self):
		events = self.get_events(self.j, self.n)

		for event in events:

			mc_track_list = [] 

			for i in range(len(event.montecarlo['particles'])):
				t = event.montecarlo['particles'][i][-1]
				mc_track = []
				for h in event.hits:
					if h.__hash__() in t:
						mc_track.append(hit_ht(h))

				mc_track_list.append(mc_track)

			for t in mc_track_list:
				x = np.array([h.z for h in t])
				y = np.array([h.r for h in t])
				z = np.polyfit(x,y,1)
				print(z)
				v1, v2 = t[0].complex, t[-1].complex
				A = (v2.imag - v1.imag)/(v2.real - v1.real) if (v2.real - v1.real) != 0 else 0
				B = A * v1.real + v1.imag

				d = abs(B)/m.sqrt(A**2 + 1)

				theta = m.asin(d/B)

				result_rho.append(d)
				result_theta.append(theta)
		return None


	# #rho max

	# r_hist = np.histogram(result_rho, bins = 50)
	# # #t_hist = np.histogram(result_theta, bins = 180)
	# plt.hist(r_hist, bins = 50)
	# plt.show()
	# print("Rho max min: ", max(result_rho), min(result_rho)) 
	# print("Theta max min: ", max(result_theta), min(result_theta))

		###########################	

			#representacion
