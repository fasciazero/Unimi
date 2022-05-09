from functools import reduce
from random import random
import math

class FGen:
    def __init__(self):
        self.n = 1
        self.i = 0
    def __iter__(self):
        self.__init__()
        return self
    def __next__(self):
        self.i += 1
        self.n *= self.i
        res = self.n
        self.i += 1
        self.n *= self.i
        return res

def alternatesum(x,y):
    if not hasattr(alternatesum, "sign"): setattr(alternatesum, "sign", False)
    alternatesum.sign = not alternatesum.sign
    return x-y if alternatesum.sign else x+y

def mysin(x, pr=5):
    return reduce(alternatesum, [x**e/f for e,f in zip(range(1,pr*2,2),FGen())])

for _, f in zip(range(10), FGen()):
    print(f)

print('\n'.join(["{:1.8f}".format(abs(mysin(t:=random(),pr=3) - math.sin(t))) for i in range(30)]))
