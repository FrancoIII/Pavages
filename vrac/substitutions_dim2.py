# francois oder le 22 juin 2017


import math


def fibo(n):
    phi = (1 + math.sqrt(5))/2
    phi_ = (1 - math.sqrt(5))/2
    return (1/(math.sqrt(5)))*(phi**n - phi_**n)


def iterer(L, n):
    m = int(fibo(n+3))
    q = int(fibo(n+2))
    d = m - q
    M = [[0 for i in range(m)] for i in range(m)]
    d_y = 0
    d_y_cond = False
    for u in range(q):
        i = q-u-1
        d_x = 0
        for j in range(q):
            if L[i][j] == 1:
                M[(i - d_y + d)%m][(j + d_x)%m] = 1
                M[(i - d_y - 1 + d) % m][(j + d_x)%m] = 2
                M[(i - d_y + d) % m][(j + d_x + 1)%m] = 3
                M[(i - d_y - 1 + d) % m][(j + d_x + 1)%m] = 4
                d_y_cond = True
                d_x += 1
            elif L[i][j] == 2:
                M[(i - d_y + d) % m][(j + d_x) % m] = 1
                M[(i - d_y + d) % m][(j + d_x + 1) % m] =3
                d_y_cond = False
                d_x += 1
            elif L[i][j] == 3:
                M[(i - d_y + d) % m][(j + d_x) % m] = 1
                M[(i - d_y - 1 + d) % m][(j + d_x) % m] = 2
            else:
                M[(i - d_y + d)%m][(j + d_x)%m] = 1
        if d_y_cond :
            d_y += 1
    return M


def affiche(M):
    for L in M:
        print(L)


def est_dans(P, G):
    for L in G:
        if P == L:
            return True
    return False


def complexité(M, n):
    K = []
    p = 0
    for i in range(len(M)-n):
        for j in range(len(M)-n):
            L = []
            for x in range(n):
                L += [M[i+x][j:j+n]]
            if not est_dans(L, K):
                p += 1
                K += [L]
    return p


M = [[1]]
for n in range(4):
    M = iterer(M, n)

affiche(M)
