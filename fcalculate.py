import pylab
from fInToOut import *
import math

OPERATORS = {
    '+': float.__add__,
    '-': float.__sub__,
    '*': float.__mul__,
    '/': float.__truediv__,
    '%': float.__mod__,
    '^': float.__pow__,
}


def calculate(d):
    v = list(inToOut(d))
    stack = []
    i = 0
    k = 0
    end = False
    while not end:
        k = 0
        c = v[i]
        if c in ['+', '-', '/', '*', '^', '%']:
            a = stack.pop()
            b = stack.pop()
            k = OPERATORS[c](b, a)
        else:
            k = float(c)
        stack.append(k)
        i = i + 1
        if i >= len(v):
            end = True
    return k


from pylab import *

xmin = -10
xmax = 10
dx = 0.01
xlist = mlab.frange(xmin, xmax, dx)
xlist = list(xlist)


def func(d):
    global xlist
    d = d.replace(' ', '')
    d = str(d)
    h = d
    x1 = []
    z = []
    for i in xlist:
        g = 0

        while g < len(d):
            if d[g] == 'x':
                if i < 0:
                    d = d[:g] + '(0' + str(i) + ')' + d[g + 1:]
                else:
                    d = d[:g] + str(i) + d[g + 1:]
            g += 1

        try:
            l = calculate(d)
            if (-10 <= l <= 10):
                z.append(l)
                x1.append(i)
        except:
            pass



        d = h
    print(len(xlist), '\n', len(z))
    pylab.plot(x1, z)
    savefig('plot')
    plt.clf()
