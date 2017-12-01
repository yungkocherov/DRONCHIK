import pylab
from math import *
import copy
from tkinter import *
from fInToOut import *
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


xmin = -100
xmax = 100
dx = 1
xlist = mlab.frange(xmin, xmax, dx)
xlist = list(xlist)


def func(d):
    root = Tk()
    d = str(d)
    h = d

    z = []
    for i in xlist:

            for g in range(len(d)):
                if d[g] == 'x':
                    if i<0 :
                        d = d[:g] +'(0'+str(i) + ')' + d[g+1:]
                    else:
                        d = d[:g] + str(i) + d[g + 1:]
            try:
                l = calculate(d)
            except:
                pass
            z.append(l)
            print(l,'    ', i)
            d = h

    pylab.plot(xlist, z)
    savefig('plot')
    plt.clf()