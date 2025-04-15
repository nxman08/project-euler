import math 
def pr(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True


def concat_prime(a, b):
    return pr(int(str(a) + str(b))) and pr(int(str(b) + str(a)))

primes = [p for p in range(2, 10000) if pr(p)]

for a in primes:
    for b in primes:
        if b <= a or not concat_prime(a, b):
            continue
        for c in primes:
            if c <= b or not all(concat_prime(x, c) for x in [a, b]):
                continue
            for d in primes:
                if d <= c or not all(concat_prime(x, d) for x in [a, b, c]):
                    continue
                for e in primes:
                    if e <= d or not all(concat_prime(x, e) for x in [a, b, c, d]):
                        continue
                    print(f"Found set: {a}, {b}, {c}, {d}, {e}")
                    print(f"Sum: {a + b + c + d + e}")
                    exit() 