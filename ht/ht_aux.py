import matplotlib.pyplot as plt
import numpy as np
from event_model import *
import cmath as cm
import math as m


# class accumulator():
# 	def __init__(self, theta_max, theta_min, n_rotations, rho = None, angles = None):
# 		self.theta_max = theta_max
# 		self.theta_min = theta_min	
# 		self.angles = list(map(lambda x: m.radians(x),list(range(self.theta_min, self.theta_max))))

# 		if not rho:
# 			self.rho = list(range(-750,750))
# 			#self.acc = [[(0, []) for x in range(len(self.angles)+1)] for y in range(len(self.rho))]
# 			self.acc = [[[0, []] for x in range(len(self.rho))] for y in range(len(self.angles)+1)]

# 	def theta_to_x(self, a):
# 		r = 0
# 		for i in range(len(self.angles)):
# 			if a >= self.angles[i]: r = i
# 		return r

# 	def rho_to_y(self, a):
# 		r = 0
# 		for i in range(len(self.rho)):
# 			if a >= self.rho[i]: r = i
# 		return r

# 	def get_angles(self):
# 		return list(self.angles)

# 	def inc(self, hit):
# 		c = cm.polar(hit.complex)
# 		coord_x = self.theta_to_x(c[1])
# 		coord_y = self.rho_to_y(c[0])
# 		self.acc[coord_x][coord_y][1].append(hit)
# 		self.acc[coord_x][coord_y][0] += 1
# 		return None

# 	def get_params_list(self, threshold):
# 		r = list()
# 		for i in range(len(self.angles)+1):
# 			for j in range(len(self.rho)):
# 				pass
# 		return r

# 	def get_tracks(self, umbral):
# 		l = list()
# 		for a in self.acc:
# 			for b in a:
# 				if b[0] > umbral: 
# 					l.append(b[1])

# 		return l

# 	def __repr__(self):
# 		s = ""
# 		for a in self.acc:
# 			for b in a:
# 				if b[0] > 1: print(b)
# 		return s

class hit_ht(hit):
	def __init__(self, h):
		hit.__init__(self, h.x, h.y, h.z, h.id, h.hit_number, h.sensor_number)
		self.complex_ht = complex(self.z, self.r)

	def c_rotate(self, angle):
		self.complex_ht *= complex(m.cos(angle), m.sin(angle))
		return None

	def c_get_real(self):
		return self.complex_ht.real

	def c_get_imag(self):
		return self.complex_ht.imag

	def c_ht_reset(self):
		self.complex_ht = complex(self.z, self.r)
		return None

	def __getattr__(self, name):
		if name == 'phi':
			return m.atan2(self.x, self.y)
		elif name == 'r':
			return m.sqrt((self.x)**2 + (self.y)**2)
		elif name == 'complex':
			return self.complex_ht
		else:
			raise  AttributeError(name)

	def __repr__(self):
		return "#" + str(self.hit_number) + " {" + str(self.r) + ", " + \
				str(self.phi) + ", " + str(self.z) + "}"

def rotation(vble, angle):
	return None

def rotate_theta(hit, angle):

	return None

def rotate_eta():
	return None

def rotate(z, angle):
	return z * complex(m.cos(angle), m.sin(angle))

def argand(a):
    for x in range(len(a)):
        plt.plot([0,a[x].real],[0,a[x].imag],'bo', ls = 'none', label='python')

    limit=np.max(np.ceil(np.absolute(a))) 
    plt.xlim((-limit,limit))
    plt.ylim((-limit,limit))
    plt.ylabel('Imaginary')
    plt.xlabel('Real')
    plt.show()

def histogram(hits, min_a, max_a, bin_size):

	r = list(range(min_a, max_a, bin_size))
	brackets = list(zip(r[0:-1], r[1:]))

	res = {n:[z for z in hits if z.c_get_imag() >= n[0] and z.c_get_imag() < n[1]] for n in brackets}

	return {k:v for k,v in res.items() if len(v) > 0}


def histogram_n(hits, min_a, max_a, bin_size):

	r = list(range(min_a, max_a, bin_size))
	brackets = list(zip(r[0:-1], r[1:]))


	return {tuple(brackets[n]):0 for n in range(len(brackets))}

		# testing 1

		#for e in classified_hits_cmp:
		#	argand(e) 

		# testing 2

		# for e in classified_hits_cmp[0:5]:
		# 	graph.plot([x.real for x in e], [x.imag for x in e], 'o-', ls = 'none')

		# eje_x = None

		# graph.show()


		# testing 3