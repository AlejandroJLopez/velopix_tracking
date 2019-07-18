import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ht_solver import *
from ht_solver_4 import ht_solver
from classical_solver import classical_solver

import event_model as em
import ht_pruebas as htp

import math as m

import validator_lite as vl

#utiliza los tracks del montecarlo para pasarle los hits al algoritmo

class new_event():
    def __init__(self, hits):
        self.hits = hits
    def __iter__(self):
        return iter(self.hits)

if __name__ == "__main__":

    n = 11
    j = 10
    n_bins = 32
    solutions = []

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

        new_hit_list = [] 

        for i in range(len(event.montecarlo['particles'])):
        	t = event.montecarlo['particles'][i][-1]
        	for h in event.hits:
        		if h.__hash__() in t:
        			new_hit_list.append(h)

        ht_s = ht_solver()
        event.hits = new_hit_list
        solutions = ht_s.solve(event)
        vl.validate_print(event, solutions)



        

