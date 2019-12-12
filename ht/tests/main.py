import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ht_solver import *
from ht_solver_4 import ht_solver
from classical_solver import classical_solver
import event_model as em
import ht_pruebas as htp
import math as m
import validator_lite as vl
import test_1


if __name__ == '__main__':
	prueba = test_1.Test_1()
	prueba.run()