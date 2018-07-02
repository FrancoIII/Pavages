# francois oder le 6 juin 2018


from copy import copy


def sigma(char):
    if char == 0:
        return '01'
    elif char == 1:
        return '02'
    elif char == 2:
        return '0'
    raise ValueError('Ne prends que 0, 1  ou 2 en argument')


def pav_trib_(length):
    pav = '01'
    i = 1
    while len(pav) < length:
        pav += sigma(int(pav[i]))
        i += 1
    return pav


def pav_trib(nb):
    pav = '0'
    for i in range(nb):
        pav_ = ''
        for char in pav:
            pav_ += sigma(int(char))
        pav = pav_
    return pav


def count(w, n):
    res = 0
    found = []
    for i in range(len(w) - n):
        u = w[i:i + n]
        if u not in found:
            res += 1
            found += [u]
    return res


def verifier(w_, long):
    found = []
    for i in range(len(w_) - long):
        u = w_[i:i + long]
        if u not in found:
            found += [u]
    found_1 = []
    for i in range(len(w_) - long - 1):
        u = w_[i:i + long + 1]
        if u not in found_1:
            found_1 += [u]
    res = 0
    found_2 = []
    for i in range(len(w_) - long - 2):
        u = w_[i:i + long + 2]
        if u not in found_2:
            res += 1
            found_2 += [u]
    Nrlb = dict()
    for fact in found:
        Nr = 0
        Nl = 0
        Nb = 0
        for char in ['0', '1', '2']:
            if fact + char in found_1:
                Nr += 1
            if char + fact in found_1:
                Nl += 1
            for char_ in ['0', '1', '2']:
                if char_ + fact + char in found_2:
                    Nb += 1
        Nrlb[fact] = [Nr, Nl, Nb]
    return Nrlb

wo = pav_trib_(1000)


for ln in range(20):
    print(ln, verifier(wo, ln))
