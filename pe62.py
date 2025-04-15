def isc(n):
    return int(n ** (1/3)) ** 3 == n

def solve():
    c = {}
    i = 1
    while True:
        cb = i ** 3
        k = ''.join(sorted(str(cb)))
        if k not in c:
            c[k] = []
        c[k].append(cb)
        if len(c[k]) == 5:
            return min(c[k])
        i += 1

result = solve()
print(result)
