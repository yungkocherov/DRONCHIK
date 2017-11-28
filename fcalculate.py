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


def calculate(s):
    s = InToOut(s)
    stack = []
    i = 0
    k = 0
    end = False
    while not end:
        k = 0
        c = s[i]
        if c in ['+', '-', '/', '*', '^', '%']:
            a = stack.pop()
            b = stack.pop()
            k = OPERATORS[c](b, a)
        else:
            k = float(c)
        stack.append(k)
        i = i + 1
        if i >= len(s):
            end = True
    return k


s = input()
d = InToOut(s)
z = []
v = d
xmin = -1000
xmax = 1000
dx = 1

xlist = mlab.frange(xmin, xmax, dx)

for i in xlist:
    for g in d:
        if g == 'x':
            g = str(i)
    l = calculate(d)
    z.append(l)
    d = v

pylab.plot(xlist, z)
pylab.show()