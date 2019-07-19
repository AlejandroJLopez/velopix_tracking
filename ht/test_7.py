import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from classical_solver import classical_solver
from ht_solver import *
from ht_solver_4 import ht_solver
import event_model as em
import ht_pruebas as htp

import math as m
import numpy as np
import matplotlib.pyplot as plt


import validator_lite as vl

#comprueba los tracks de Montecarlo que están dentro del rango de aceptacion

if __name__ == "__main__":

    n = 100
    j = 0
    n_bins = 32

    #todos los json

    #histograma
    result_rho = []
    result_theta = []

    for i in range(j, n):
        f = open("../velojson_5k/"+str(i)+".json")
        json_data = json.loads(f.read())
        event = em.event(json_data)
        f.close()

        print("JSON number " + str(i))

        mc_track_list = [] 

        for i in range(len(event.montecarlo['particles'])):
            t = event.montecarlo['particles'][i][-1]
            mc_track = []
            for h in event.hits:
                if h.__hash__() in t:
                    mc_track.append(hit_ht(h))

            mc_track_list.append(mc_track)

        for t in mc_track_list:
            v1, v2 = t[0].complex, t[-1].complex
            A = (v2.imag - v1.imag)/(v2.real - v1.real) if (v2.real - v1.real) != 0 else 0
            B = A * v1.real + v1.imag

            d = abs(B)/m.sqrt(A**2 + 1)

            theta = m.asin(d/B)

            result_rho.append(d)
            result_theta.append(theta)

    #rho max

    r_hist = np.histogram(result_rho, bins = 50)
    # #t_hist = np.histogram(result_theta, bins = 180)
    plt.hist(r_hist, bins = 50)
    plt.show()
    print("Rho max min: ", max(result_rho), min(result_rho)) 
    print("Theta max min: ", max(result_theta), min(result_theta))