import matplotlib.pyplot as plt
import numpy as np
import math as m
import cmath as cm
import ht_solver
from ht_aux import *
from functools import reduce


if __name__ == '__main__':


	#PRUEBA DE GIROS DE NUMEROS COMPLEJOS

	# z = complex(1.0, 0.0)

	# n_rotations = 360

	# for k in range(n_rotations+1):
	# 	angle = m.fmod(((2*m.pi/n_rotations)*k), 2*m.pi)
	# 	z_rotated = z * complex(m.cos(angle), m.sin(angle))
	# 	#plt.plot(z_rotated.real, z_rotated.imag, 'ro-', ls = 'none', label = 'complex_number', markersize = 2)
	# 	plt.plot(angle, z_rotated.imag, 'ko-', ls = 'none', label = 'complex_number', markersize = 2)

	# plt.show()





	#EJEMPLO DE RENATO HT BASICO

	n_rotations = 200
	desp = 100
	bin_size = 1
	threshold = 50

	hits = [(a+desp,b+desp) for a in range(-50, 51, 1) for b in range(-50, 51, 1) if abs(a) == abs(b)]

	hits_complex = [complex(x[0], x[1]) for x in hits]

	soluciones = list()


	for k in range(n_rotations):
		angle = m.fmod((m.pi/n_rotations)*k, 2*m.pi) - m.pi/2
		hit_rotated = [rotate(x, angle) for x in hits_complex]


		#histograma
		hit_classified = histogram(hit_rotated, -150, 230, bin_size)

		#print(hit_classified)

		hit_classified = list(filter(lambda xy: xy[0]>= threshold, hit_classified))

		if hit_classified:
			soluciones.append([hit_classified, m.degrees(angle)])
		



		#representacion

		plt.plot([m.degrees(angle) for _ in hit_rotated], [x.imag for x in hit_rotated], 'ko-', ls = 'none', markersize = 0.2)

		plt.ylim(230, -150)
		plt.grid(True)
		plt.xlabel('theta')
		plt.ylabel('imaginary part of hit_rotated')


	print(soluciones)
	plt.show()

	


