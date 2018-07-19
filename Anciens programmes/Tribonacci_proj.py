# francois oder le 4 juin 2018


import matplotlib.pyplot as plt
from copy import copy
from mpl_toolkits.mplot3d import Axes3D
from math import sqrt


def sigma(char):
    if char == 0:
        return [0, 1]
    elif char == 1:
        return [0, 2]
    elif char == 2:
        return [0]
    raise ValueError('Ne prends que 0, 1  ou 2 en argument')


def pav_trib(length):
    pav = [0, 1]
    i = 1
    while len(pav) < length:
        pav += sigma(pav[i])
        i += 1
    return pav


def plot(w):
    chem = gen_chem(w)
    x = []
    y = []
    z = []
    for point in chem:
        x += [point[0]]
        y += [point[1]]
        z += [point[2]]
    ax.plot(x, y, z, 'w:')
    for i in range(1, len(chem)):
        if chem[i][3] == 1:
            ax.plot([x[i]], [y[i]], [z[i]], 'ro')
        elif chem[i][3] == 0:
            ax.plot([x[i]], [y[i]], [z[i]], 'go')
        else:
            ax.plot([x[i]], [y[i]], [z[i]], 'bo')
    num0 = w.count(0)
    num1 = w.count(1)
    num2 = w.count(2)
    ax.plot([0, num0], [0, num1], [0, num2], 'y-')


def vect_dir(w):
    num0 = w.count(0)
    num1 = w.count(1)
    num2 = w.count(2)
    norm = sqrt(num0**2 + num1**2 + num2**2)
    return [num0/norm, num1/norm, num2/norm]


def gen_chem(w):
    chem = [[0, 0, 0]]
    current = [0, 0, 0, None]
    for char in w:
        current[char] += 1
        current[3] = char
        chem += [copy(current)]
    return chem


def proj_orth(point, vect):
    scal = point[0]*vect[0] + point[1]*vect[1] + point[2]*vect[2]
    comp0 = scal*vect[0]
    comp1 = scal*vect[1]
    comp2 = scal*vect[2]
    return [point[0] - comp0, point[1] - comp1, point[2] - comp2]


def plot_proj(w):
    vect = vect_dir(w)
    chem = gen_chem(w)
    for point in chem[1:]:
        p = proj_orth(point, vect)
        if point[3] == 1:
            ax.plot([p[0]], [p[1]], [p[2]], 'ro')
        elif point[3] == 0:
            ax.plot([p[0]], [p[1]], [p[2]], 'go')
        else:
            ax.plot([p[0]], [p[1]], [p[2]], 'bo')


def norm(vect):
    res = vect[0]**2 + vect[1]**2 + vect[2]**2
    return sqrt(res)


def bon_dir(w):
    num0 = w.count(0)
    num1 = w.count(1)
    num2 = w.count(2)
    orth1_0 = - num1
    orth1_1 = num0
    orth1_2 = 0
    orth2_0 = - num0*num2
    orth2_1 = - num1*num2
    orth2_2 = num0**2 + num1**2
    div1 = norm([num0, num1, num2])
    div2 = norm([orth1_0, orth1_1, orth1_2])
    div3 = norm([orth2_0, orth2_1, orth2_2])
    dir = [num0/div1, num1/div1, num2/div1]
    orth1 = [orth1_0/div2, orth1_1/div2, orth1_2/div2]
    orth2 = [orth2_0/div3, orth2_1/div3, orth2_2/div3]
    return dir, orth1, orth2


def scal(point, vect):
    return point[0]*vect[0] + point[1]*vect[1] + point[2]*vect[2]


def plot_2D_proj(w):
    (dir, vectX, vectY) = bon_dir(w)
    chem = gen_chem(w)
    for point in chem[1:]:
        p = proj_orth(point, dir)
        x = [scal(p, vectX)]
        y = [scal(p, vectY)]
        if point[3] == 1:
            plt.plot(x, y, 'ro')
        elif point[3] == 0:
            plt.plot(x, y, 'go')
        else:
            plt.plot(x, y, 'bo')


def bon(dir):
    num0 = dir[0]
    num1 = dir[1]
    num2 = dir[2]
    orth1_0 = - num1
    orth1_1 = num0
    orth1_2 = 0
    orth2_0 = - num0*num2
    orth2_1 = - num1*num2
    orth2_2 = num0**2 + num1**2
    div1 = norm([num0, num1, num2])
    div2 = norm([orth1_0, orth1_1, orth1_2])
    div3 = norm([orth2_0, orth2_1, orth2_2])
    res_dir = [num0/div1, num1/div1, num2/div1]
    orth1 = [orth1_0/div2, orth1_1/div2, orth1_2/div2]
    orth2 = [orth2_0/div3, orth2_1/div3, orth2_2/div3]
    return res_dir, orth1, orth2


def plot_2D_proj_t(w, dir):
    (n_dir, vectX, vectY) = bon(dir)
    chem = gen_chem(w)
    for point in chem[1:]:
        p = proj_orth(point, n_dir)
        x = [scal(p, vectX)]
        y = [scal(p, vectY)]
        if point[3] == 1:
            plt.plot(x, y, 'ro')
        elif point[3] == 0:
            plt.plot(x, y, 'go')
        else:
            plt.plot(x, y, 'bo')


tri_const = 1.8392867552141611321
tri_dir = [1/tri_const, 1/tri_const**2, 1/tri_const**3]


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


wo = pav_trib(10)
plot(wo)
plot_proj(wo)


plt.show()


w = pav_trib(10)
plot_2D_proj(w)


plt.show()


w_ = pav_trib(100000)
plot_2D_proj_t(w_, tri_dir)


plt.show()
