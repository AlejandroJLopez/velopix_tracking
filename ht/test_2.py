import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ht_solver import *
from ht_solver_3 import ht_solver
import event_model as em
import ht_pruebas as htp

import validator_lite as vl


if __name__ == "__main__":

    n = 9
    j = 8

    #todos los json

    for i in range(j, n):
        f = open("../velojson/"+str(i)+".json")
        json_data = json.loads(f.read())
        event = em.event(json_data)
        f.close()
        solutions = {"ht":[]}

        print("JSON number " + str(i))
        for h in event.hits: 
        	solutions["ht"].append(track([h]))
        print("Validacion")

        vl.validate_print([json_data], [solutions["ht"]])