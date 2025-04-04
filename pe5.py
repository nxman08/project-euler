import math

def lcm(a, b):
    return a * b // math.gcd(a, b)  

def sm(n):
    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)
    return result

print(sm(20))
