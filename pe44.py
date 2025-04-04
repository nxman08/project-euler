import math

def is_pentagonal(n):
    if n <= 0:
        return False
    k = (1 + math.sqrt(1 + 24 * n)) / 6
    return k.is_integer()

def pentagonal(n):
    return n * (3 * n - 1) // 2

pentagonals = [pentagonal(i) for i in range(1, 3000)]  # Generate first 3000 pentagonal numbers

min_diff = float('inf')

for k in range(len(pentagonals)):
    for j in range(k):
        pk, pj = pentagonals[k], pentagonals[j]
        if is_pentagonal(pk - pj) and is_pentagonal(pk + pj):
            min_diff = min(min_diff, pk - pj)

print("Minimum difference:", min_diff)
