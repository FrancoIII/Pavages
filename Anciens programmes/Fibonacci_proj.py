# francois oder le 29 mai 2018


import matplotlib.pyplot as plt
from copy import copy
from math import sqrt


def sigma(char):
    if char == 0:
        return [0, 1]
    elif char == 1:
        return [0]
    raise ValueError('0 ou 1 en argument')


def pav_fib(length):
    pav = [0, 1]
    i = 1
    while len(pav) < length:
        pav += sigma(pav[i])
        i += 1
    return pav


def plot(chem):
    x = []
    y = []
    for point in chem:
        x += [point[0]]
        y += [point[1]]
    plt.plot(x, y, '')
    for i in range(1, len(chem)):
        if chem[i][2]:
            plt.plot(x[i], y[i], 'ro')
        else:
            plt.plot(x[i], y[i], 'go')


def plot_pav(w):
    chem = [[0, 0]]
    current = [0, 0, None]
    for char in w:
        current[char] += 1
        current[2] = char
        chem += [copy(current)]
    plot(chem)
    # line(w)
    t_line(chem)
    plt.show()


def line(w):
    num0 = w.count(0)
    num1 = w.count(1)
    plt.plot([0, num0], [0, num1], 'y-')


def t_line(chem):
    direct = 2/(1 + sqrt(5))
    plt.plot([0, chem[-1][0]], [0, chem[-1][0] * direct], 'b-')


def scal_(vect1, vect2):
    return vect1[0]*vect2[0] + vect1[1]*vect2[1]


def proj_plot(w, orth_dir):
    chem = [[0, 0]]
    current = [0, 0, None]
    for char in w:
        current[char] += 1
        current[2] = char
        chem += [copy(current)]
    proj_set = []
    for point in chem[1:]:
        scal = scal_(point, orth_dir)
        proj = [scal*orth_dir[0], scal*orth_dir[1], point[2]]
        proj_set += [proj.copy()]
    x = []
    y = []
    for point in proj_set:
        x += [point[0]]
        y += [point[1]]
    for i in range(1, len(proj_set)):
        if proj_set[i][2]:
            plt.plot(x[i], y[i], 'r.')
        else:
            plt.plot(x[i], y[i], 'g.')


phi = (1 + sqrt(5))/2
norm = scal_([-1, phi], [-1, phi])
orth_dir = [-1/sqrt(norm), phi/sqrt(norm)]

wo = pav_fib(50)

proj_plot(wo, orth_dir)

plot_pav(wo)
