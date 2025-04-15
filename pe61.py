t = []
n = 0
i = 1
while n < 10000:
    n = int(i * (i + 1) / 2)
    i += 1
    if len(str(n)) == 4:
        t.append(n)

s = []
n = 0
i = 1
while n < 10000:
    n = i ** 2
    i += 1
    if len(str(n)) == 4:
        s.append(n)

p = []
n = 0
i = 1
while n < 10000:
    n = int(i * (3 * i - 1) / 2)
    i += 1
    if len(str(n)) == 4:
        p.append(n)

h = []
n = 0
i = 1
while n < 10000:
    n = int(i * (2 * i - 1))
    i += 1
    if len(str(n)) == 4:
        h.append(n)

v = []
n = 0
i = 1
while n < 10000:
    n = int(i * (5 * i - 3) / 2)
    i += 1
    if len(str(n)) == 4:
        v.append(n)

o = []
n = 0
i = 1
while n < 10000:
    n = int(i * (3 * i - 2))
    i += 1
    if len(str(n)) == 4:
        o.append(n)

from itertools import permutations


others = [s, p, h, v, o]

for perm in permutations(others):
    for tr in t:
        tr_r = tr % 100
        if tr_r < 10:
            continue
        for a in perm[0]:
            if a // 100 != tr_r:
                continue
            a_r = a % 100
            if a_r < 10:
                continue
            for b in perm[1]:
                if b // 100 != a_r:
                    continue
                b_r = b % 100
                if b_r < 10:
                    continue
                for c in perm[2]:
                    if c // 100 != b_r:
                        continue
                    c_r = c % 100
                    if c_r < 10:
                        continue
                    for d in perm[3]:
                        if d // 100 != c_r:
                            continue
                        d_r = d % 100
                        if d_r < 10:
                            continue
                        for e in perm[4]:
                            if e // 100 == d_r and e % 100 == tr // 100:
                                seq = [tr, a, b, c, d, e]
                                
                                print(sum(seq))
                                exit()

