from ht_solver import *
from classical_solver import classical_solver
import event_model as em
import ht_pruebas as htp

import validator_lite as vl

if __name__ == "__main__":

    n = 1
    j = 0


    #un solo json



    #todos los json

    for i in range(j, n):
        f = open("velojson/"+str(i)+".json")
        json_data = json.loads(f.read())
        event = em.event(json_data)
        f.close()
        solutions = {}

        print("JSON number " + str(i))
        ht_solver = ht_solver()
        solutions["ht"] = ht_solver.solve(event)

        vl.validate_print([json_data], [solutions["ht"]])



    """
    tracks = [x[-1] for x in event.montecarlo['particles']]

    for e in solucion:
    	if all(x in tracks for x in e):
    		print("Encontrado")
    	else:
    		print("No encontrado")

    """