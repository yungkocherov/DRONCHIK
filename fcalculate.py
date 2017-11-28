from fInToOut import *
import pylab
from matplotlib import mlab

OPERATORS = {
    '+': float.__add__,
    '-': float.__sub__,
    '*': float.__mul__,
    '/': float.__truediv__,
    '%': float.__mod__,
    '^': float.__pow__,
}



def calculate(d):
    stack = []
    i = 0
    k = 0
    end = False
    while not end:
        k = 0
        c = d[i]
        if c in ['+', '-', '/', '*', '^', '%']:
            a = stack.pop()
            b = stack.pop()
            k = OPERATORS[c](b, a)
        else:
            k = float(c)
        stack.append(k)
        i = i + 1
        if i >= len(d):
            end = True
    return (k)





s = input()
d = InToOut(s)
z = []
v = d
xmin = 1
xmax = 15
dx = 1
xlist = mlab.frange(xmin, xmax, dx)
for i in xlist:
    v = d
    for g in range (len(v)):
        if v[g] == 'x':
            v[g] = i

    print(v)
    '''l = calculate(d)'''
    '''z.append(l)'''
print(z)
'''
pylab.plot(xlist, z)
pylab.show()
'''
