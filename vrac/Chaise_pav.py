# francois oder le 7 juin 2017


import matplotlib.pyplot as plt
import numpy as np
import cv2
from copy import deepcopy
import json


def iterer(l, n):
    m = 2**(n+1)
    q = 2**n
    d = m - q
    pav_ = np.zeros((m, m))
    d_y = 0
    for u in range(q):
        i = q-u-1
        d_x = 0
        for j in range(q):
            if l[i][j] == 0:
                pav_[(i - d_y + d) % m, (j + d_x) % m] = 0
                pav_[(i - d_y - 1 + d) % m, (j + d_x) % m] = 2
                pav_[(i - d_y + d) % m, (j + d_x + 1) % m] = 1
                pav_[(i - d_y - 1 + d) % m, (j + d_x + 1) % m] = 0
                d_x += 1
            elif l[i][j] == 1:
                pav_[(i - d_y + d) % m, (j + d_x) % m] = 0
                pav_[(i - d_y - 1 + d) % m, (j + d_x) % m] = 1
                pav_[(i - d_y + d) % m, (j + d_x + 1) % m] = 1
                pav_[(i - d_y - 1 + d) % m, (j + d_x + 1) % m] = 3
                d_x += 1
            elif l[i][j] == 2:
                pav_[(i - d_y + d) % m, (j + d_x) % m] = 0
                pav_[(i - d_y - 1 + d) % m, (j + d_x) % m] = 2
                pav_[(i - d_y + d) % m, (j + d_x + 1) % m] = 2
                pav_[(i - d_y - 1 + d) % m, (j + d_x + 1) % m] = 3
                d_x += 1
            else:
                pav_[(i - d_y + d) % m, (j + d_x) % m] = 3
                pav_[(i - d_y - 1 + d) % m, (j + d_x) % m] = 2
                pav_[(i - d_y + d) % m, (j + d_x + 1) % m] = 1
                pav_[(i - d_y - 1 + d) % m, (j + d_x + 1) % m] = 3
                d_x += 1
        d_y += 1
    return pav_


def gen_pav(nb_iter):
    name = 'Chaise'
    temp = np.zeros((1, 1))
    for n in range(nb_iter):
        temp = iterer(temp, n)
        print(n)
        (n, n) = temp.shape
        pav = []
        for line in temp:
            pav += [list(line)]
        filename = name + str(n)
        file = open(filename, 'w')
        json.dump(pav, file)
        file.close()
    return temp


def is_egal(act, array):
    assert(act.shape == array.shape)
    (n, m) = act.shape
    for x in range(n):
        for y in range(m):
            if act[x, y] != array[x, y]:
                return False
    return True


def is_in(act, seen):
    for array in seen:
        if is_egal(act, array):
            return True
    return False


def count(pav, n, m):
    (len_x, len_y) = pav.shape
    seen = []
    res = 0
    for x in range(len_x - n + 1):
        for y in range(len_y - m + 1):
            act = deepcopy(pav[x:(x + n), y:(y + m)])
            if not is_in(act, seen):
                res += 1
                seen += [deepcopy(act)]
    return res


# ça marche pas :'(
def representer(pav):
    n = len(pav)

    def valid(x, y):
        return n > x >= 0 and n > y >= 0

    res = np.zeros((2*n, 2*n))
    dec_x = np.zeros((n, n))
    dec_y = np.zeros((n, n))
    for x, line in enumerate(pav):
        for y, elt in enumerate(line):
            if int(elt) == 0:
                d_x = int(dec_x[x, y])
                d_y = int(dec_y[x, y])
                print(x, d_x, y, d_y)
                res[x + d_x, y + d_y] = 1
                res[x + d_x + 1, y + d_y] = 1
                res[x + d_x, y + d_y + 1] = 1
                for i in range(len(dec_y[x:, y])):
                    if valid(x + i, y):
                        dec_x[x + i, y] += 1
                for j in range(len(dec_x[x, y:])):
                    if valid(x, y + j):
                        dec_y[x, y + j] += 1
            if int(elt) == 1:
                d_x = int(dec_x[x, y])
                d_y = int(dec_y[x, y])
                print(x, d_x, y, d_y)
                res[x + d_x, y + d_y] = 2
                res[x + d_x, y + d_y + 1] = 2
                res[x + d_x + 1, y + d_y + 1] = 2
                """
                for i in range(len(dec_y[x:, y])):
                    if valid(x + i, y):
                        dec_x[x + i, y] += 1
                """
                for j in range(len(dec_x[x, y:])):
                    if valid(x, y + j):
                        dec_y[x, y + j] += 1
                    if valid(x + 1, y + j + 1):
                        dec_y[x + 1, y + j + 1] += 1
            if int(elt) == 2:
                d_x = int(dec_x[x, y])
                d_y = int(dec_y[x, y])
                print(x, d_x, y, d_y)
                res[x + d_x, y + d_y] = 3
                res[x + d_x + 1, y + d_y] = 3
                res[x + d_x + 1, y + d_y + 1] = 3
                for i in range(len(dec_y[x:, y])):
                    if valid(x + i, y):
                        dec_x[x + i, y] += 1
                """
                for j in range(len(dec_x[x, y:])):
                    if valid(x + 1, y + j):
                        dec_y[x + 1, y + j] += 1
                """
            if int(elt) == 3:
                d_x = int(dec_x[x, y])
                d_y = int(dec_y[x, y])
                print(x, d_x, y, d_y)
                res[x + d_x + 1, y + d_y + 1] = 4
                res[x + d_x + 1, y + d_y] = 4
                res[x + d_x, y + d_y + 1] = 4
                """
                for i in range(len(dec_y[x:, y])):
                    if valid(x + i, y + 1):
                        dec_x[x + i, y + 1] += 1
                for j in range(len(dec_x[x, y:])):
                    if valid(x + 1, y + j):
                        dec_y[x + 1, y + j] += 1
                """
            print(res, '\n', dec_x, '\n', dec_y)
    return res


def representer_pav(pav):
    if pav.shape == (2, 2):
        res = np.zeros((2, 2))
        for x, line in enumerate(pav):
            for y, elt in enumerate(line):
                res[x, y] = elt + 1
        return res
    (n, n) = pav.shape
    sep = int(n/2)
    res = np.zeros((n, n))
    pav_splt1 = pav[:sep, :sep]
    pav_splt2 = pav[sep:, :sep]
    pav_splt3 = pav[:sep, sep:]
    pav_splt4 = pav[sep:, sep:]
    n_pav1 = np.zeros((n, n))
    n_pav1[:sep, :sep] = pav_splt1
    n_pav1[sep:, :sep] = pav_splt1
    n_pav1[:sep, sep:] = pav_splt1
    n_pav1[sep:, sep:] = pav_splt4
    res[:sep, :sep] = representer_pav(n_pav1)
    n_pav2 = np.zeros((n, n))
    n_pav2[:sep, :sep] = pav_splt2
    n_pav2[sep:, :sep] = pav_splt2
    n_pav2[:sep, sep:] = pav_splt4
    n_pav2[sep:, sep:] = pav_splt2
    res[sep:, :sep] = representer_pav(n_pav2)
    n_pav3 = np.zeros((n, n))
    n_pav3[:sep, :sep] = pav_splt3
    n_pav3[sep:, :sep] = pav_splt4
    n_pav3[:sep, sep:] = pav_splt3
    n_pav3[sep:, sep:] = pav_splt3
    res[:sep, sep:] = representer_pav(n_pav3)
    return res


def image_pav(pav, taille, filename):

    def creer_im(longueur, hauteur):
        return np.zeros((longueur, hauteur, 3))

    def colorer(image, longueur, hauteur, haut_gauche_ligne, haut_gauche_colonne, b, v, r):
        l = len(image)
        c = len(image[0])
        for i in range(hauteur):
            for j in range(longueur):
                image[(i + haut_gauche_ligne) % l, (j + haut_gauche_colonne) % c] = [b, v, r]

    n = len(pav)
    im = creer_im(n*taille, n*taille)
    for x, line in enumerate(pav):
        for y, elt in enumerate(line):
            b, v, r = 0, 0, 0
            if elt == 1:
                b, v, r = 255, 0, 0
            if elt == 2:
                b, v, r = 0, 255, 0
            if elt == 3:
                b, v, r = 0, 0, 255
            if elt == 4:
                b, v, r = 0, 255, 255
            colorer(im, taille, taille, x*taille, y*taille, b, v, r)

    cv2.imwrite(filename, im)

    return im

"""
iteration = 10
with open('Chaise' + str(2**iteration), 'r') as file:
    pav = json.load(file)
    pav = np.array(pav)
"""

# r_pav = representer(pav)
# r_pav_ = representer_pav(pav)
# im = image_pav(r_pav, 50)
# im_ = image_pav(r_pav_, 10)

# cv2.imwrite('im1.jpg', im)
# cv2.imwrite('im2.jpg', im_)

# n, m = 6, 6
# comp = np.zeros((n, m))
# for i in range(n):
#     for j in range(m):
#         p = count(pav, i + 1, j + 1)
#         comp[i, j] = p
# print(comp)


N = 10
"""
for n in range(N):
    comp = count(pav, n, n)
    maj = n**2
    print(n, comp, maj, 2*maj, 3*maj, 4*maj, 5*maj, 6*maj)
"""

comps = [1, 4, 19, 52, 107, 176, 271, 380, 499, 640]
Ns = [i for i in range(N)]

plt.plot(Ns, comps)
plt.show()
