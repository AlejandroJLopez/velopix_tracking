from test_model import *

class Test_1(Test):
	"""Prueba de la transformada de Hough"""
	def __init__(self, plot = True, n_rotations = 200, desp = 100, bin_size = 1, threshold = 50):
		super.__init__(plot)
		self.n_rotations = n_rotations
		self.desp = desp
		self.bin_size = bin_size
		self.threshold = threshold

	def run(self)
		hits = [(a+self.desp,b+self.desp) for a in range(-50, 51, 1) for b in range(-50, 51, 1) if abs(a) == abs(b)]
		hits_complex = [complex(x[0], x[1]) for x in hits]
		soluciones = list()

		for k in range(self.n_rotations):
			angle = m.fmod((m.pi/self.n_rotations)*k, 2*m.pi) - m.pi/2
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

