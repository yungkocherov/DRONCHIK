import math
import pylab
from fcalculate import *
from matplotlib import mlab

s = input()
v = s
z = []
for i in range(-5, 5):
    v = v.replace('x', str(i))
    print(v)
    v = s