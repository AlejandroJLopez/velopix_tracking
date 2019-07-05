import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ht_solver import *
from ht_solver_3 import ht_solver
from classical_solver import classical_solver
import os, sys

import event_model as em
import ht_pruebas as htp

import validator_lite as vl


if __name__ == "__main__":

    n = 5
    j = 4
    t_of_s = "ht"

    #todos los json

    for i in range(j, n):
        f = open("../velojson/"+str(i)+".json")
        json_data = json.loads(f.read())
        event = em.event(json_data)
        f.close()
        solutions = {}

        print("JSON number " + str(i))


        classical = ht_solver()
        solutions[t_of_s] = classical.solve(event)
        # ht_s = ht_solver()
        # solutions['classical'] = ht_s.solve(event)

        print("Validacion propia")

        track_count = 0
        correct_track_count = 0

        s_hits = [set(x.hits) for x in solutions[t_of_s]]

        for i in range(len(event.montecarlo['particles'])):
        	t = event.montecarlo['particles'][i][-1]
        	mc_track = []
        	for h in event.hits:
        		if h.__hash__() in t:
        			mc_track.append(h)

        	track_count += 1

        	if set(mc_track) in s_hits:
        		correct_track_count += 1

        	
        print("track totales: ", track_count)
        print("tracks corectamente reconstruidos: ", correct_track_count)