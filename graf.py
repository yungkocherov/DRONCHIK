import math
import pylab
from fcalculate import *
from matplotlib import mlab

s = input()

z = []
v = s



for i in range(-20, 20):
    v = v.replace('x', str(i))
    l = calculate(v)
    print(l)
    z.append(l)
    v = s

'''

# Интервал изменения переменной по оси X
xmin = -20.0
xmax = 20.0
# Шаг между точками
dx = 0.01

# !!! Создадим список координат по оси X на отрезке [-xmin; xmax], включая концы
xlist = mlab.frange(xmin, xmax, dx)

# Вычислим значение функции в заданных точках
ylist = [calculate(s) for x in xlist]
# !!! Нарисуем одномерный график
pylab.plot(xlist, z)

# !!! Покажем окно с нарисованным графиком
pylab.show()
'''