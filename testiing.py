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
    ''' s = s.replace('-','(0-')
        while c < len(s):
            if s[c] == '-':
                k=c
                while '0' <= s[k+1]<= '9':
                    k=k+1
                s = s[:k+1]+')'+s[k+1:]
            c+=1'''