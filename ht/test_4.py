import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ht_solver import *
from ht_solver_3 import ht_solver
from classical_solver import classical_solver

import event_model as em
import ht_pruebas as htp

import math as m

import validator_lite as vl


def phi_hit(x,y):
    return 

#comprueba el número de tracks completamente contenidos en los bins

if __name__ == "__main__":

    n = 13
    j = 12
    n_bins = 32

    #todos los json

    for i in range(j, n):
        f = open("../velojson/"+str(i)+".json")
        json_data = json.loads(f.read())
        event = em.event(json_data)
        f.close()

        print("JSON number " + str(i))

        #crea los bins

        phi_bin = [((2*m.pi)/n_bins) * n - m.pi for n in range(n_bins + 1)]
        bins = list(zip(phi_bin[:-1], phi_bin[1:]))

        #crea las variables
        track_count = 0
        f_c_track = 0

        for i in range(len(event.montecarlo['particles'])):
        	t = event.montecarlo['particles'][i][-1]
        	mc_track = []
        	for h in event.hits:
        		if h.__hash__() in t:
        			mc_track.append(h)

        	track_count += 1

            map(lambda x: [n for n,a in enumerate(bins) if ])

        	if all():
        		f_c_track += 1

        	
        print("tracks totales: ", track_count)
        print("tracks completamente contenidos en un bin: ", f_c_track)
        print("porcentaje: ", 100*f_c_track/track_count)