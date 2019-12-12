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

class Test_1(Test):
	"""Prueba de la transformada de Hough"""
	def __init__(self, n_rotations = 120, desp = 100, bin_size = 1, threshold = 50, plot = True):
		super().__init__(plot = plot)
		self.n_rotations = n_rotations
		self.desp = desp
		self.bin_size = bin_size
		self.threshold = threshold
		self.plot = plot

	def run(self):
		hits = [(a+self.desp,b+self.desp) for a in range(-50, 51, 1) for b in range(-50, 51, 1) if abs(a) == abs(b)]
		hits_complex = [complex(*h) for h in hits]
		soluciones = list()

		if self.plot:
			plt.plot([x[0] for x in hits], [x[1] for x in hits], marker= 's', markersize = 3, linestyle = 'None', color = 'black')
			plt.xlabel('x')
			plt.ylabel('y')
			plt.show()


		for k in range(self.n_rotations):
			angle = m.fmod((m.pi/self.n_rotations)*k, 2*m.pi) - m.pi/2

			hit_rotated = [rotate(x, angle) for x in hits_complex]
			#histograma
			hit_classified = histogram(hit_rotated, -150, 230, self.bin_size)

			#print(hit_classified)

			hit_classified = list(filter(lambda xy: xy[0]>= self.threshold, hit_classified))

			if hit_classified:
				soluciones.append([hit_classified, m.degrees(angle)])

			#representacion
			if self.plot:
				plt.plot([m.degrees(angle) for _ in hit_rotated], [x.imag for x in hit_rotated], 'ko-', ls = 'none', markersize = 0.2)
				plt.ylim(230, -150)
				plt.grid(True)
				plt.xlabel(r"$\dot{\Theta}$[grados]")
				plt.ylabel('parte imaginaria de hit_rotated')
		plt.show()


		return soluciones
