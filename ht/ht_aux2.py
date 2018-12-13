import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from test_1 import *
import event_model as em
import json

if __name__ == '__main__':
    test = test_1(12, 32)



    test.run()
    # with open('data_test_1.json', 'w') as fp:
    #     json.dump(test, fp)
        