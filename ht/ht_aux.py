import matplotlib.pyplot as plt
import numpy as np
from event_model import *
import cmath as cm
import math as m


class p_process():

	@staticmethod
	def clean(hit_list):
		""""""
		track_list = list(filter(lambda x: len(x) > 0, hit_list))
		new_track_list = []

		while (track_list):
			t = track_list[0]
			x = np.array([h.z for h in t])
			y = np.array([h.r for h in t])
			z = np.polyfit(x,y,1, full = True)

			if z[1] and z[1]/len(t) >=(0.005):
				track_list.pop(0)
			else:
				new_t = track_list.pop(0)

				new_track_list.append(new_t)
		return new_track_list

	@staticmethod
	def split(hits):
		track = list(sorted(hits, key = lambda x: x.sensor_number))
		new_tracks = []

		i = 0
		for n,h in enumerate(track):
			if n>0 and h.sensor_number - track[n-1].sensor_number > 4:
				new_tracks.append(hits[i:n])
				i = n
		new_tracks.append(hits[i:])
		return new_tracks

	@staticmethod
	def compatible(hits):
		# track = sorted(hits, key = lambda x: x.sensor_number)

		# for n,h in enumerate(hits):
		# 	if n > 0 and abs(h.sensor_number - hits[n-1].sensor_number) > 1:
		# 		print("sensor distance: ", h.sensor_number - hits[n-1].sensor_number)

		return True

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

	res = {n:[z for z in hits if z.imag >= n[0] and z.imag < n[1]] for n in brackets}

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