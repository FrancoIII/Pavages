# francois oder le 11 juillet 2017



def iterer(L, n):
    m = 2**(n+1)
    q = 2**n
    d = m - q
    M = [[0 for i in range(m)] for i in range(m)]
    d_y = 0
    for u in range(q):
        i = q-u-1
        d_x = 0
        for j in range(q):
            if L[i][j] == 0:
                M[(i - d_y + d)%m][(j + d_x)%m] = 0
                M[(i - d_y - 1 + d) % m][(j + d_x)%m] = 2
                M[(i - d_y + d) % m][(j + d_x + 1)%m] = 1
                M[(i - d_y - 1 + d) % m][(j + d_x + 1)%m] = 0
                d_x += 1
            elif L[i][j] == 1:
                M[(i - d_y + d)%m][(j + d_x)%m] = 0
                M[(i - d_y - 1 + d) % m][(j + d_x)%m] = 1
                M[(i - d_y + d) % m][(j + d_x + 1)%m] = 1
                M[(i - d_y - 1 + d) % m][(j + d_x + 1)%m] = 3
                d_x += 1
            elif L[i][j] == 2:
                M[(i - d_y + d)%m][(j + d_x)%m] = 0
                M[(i - d_y - 1 + d) % m][(j + d_x)%m] = 2
                M[(i - d_y + d) % m][(j + d_x + 1)%m] = 2
                M[(i - d_y - 1 + d) % m][(j + d_x + 1)%m] = 3
                d_x += 1
            else:
                M[(i - d_y + d)%m][(j + d_x)%m] = 3
                M[(i - d_y - 1 + d) % m][(j + d_x)%m] = 2
                M[(i - d_y + d) % m][(j + d_x + 1)%m] = 1
                M[(i - d_y - 1 + d) % m][(j + d_x + 1)%m] = 3
                d_x += 1
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

M = [[0]]
for n in range(7):
    M = iterer(M, n)

print(M)

#for i in range(10):
#    print(M)
#    print(complexité(M, i))
