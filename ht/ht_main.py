import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ht_solver import *
from ht_solver_4 import ht_solver
import event_model as em
import ht_pruebas as htp

import validator_lite as vl

if __name__ == "__main__":

    n = 10
    j = 0

    #todos los json
    all_json, all_solutions = [], []
    for i in range(j, n):
        f = open("../velojson_5k/"+str(i)+".json")
        json_data = json.loads(f.read())
        event = em.event(json_data)
        f.close()
        solutions = {}

        print("JSON number " + str(i))
        ht_s = ht_solver()
        solutions["ht"] = ht_s.solve(event)

        all_json.append(json_data)
        all_solutions.append(solutions["ht"])


    print("Validación")
    vl.validate_print(all_json, all_solutions)