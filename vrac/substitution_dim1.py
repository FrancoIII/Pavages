# francois oder le 17 juin 2017


def creer_w(n):
    w = '0'
    for i in range(n):
        t_w = ''
        for x in w:
            if x == '0':
                t_w += '01'
            else:
                t_w += '10'
        w = t_w
    return w


def compter(w,n):
    res = 0
    L = []
    for i in range(len(w)-n):
        u = w[i:i+n]
        if u not in L:
            res += 1
            L += [u]
    return res

w = creer_w(11)
#for k in range(50):
#    print(k,compter(w, k))

print(w)