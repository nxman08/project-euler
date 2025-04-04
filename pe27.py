import math

def is_prime(n):
    if n < 2: 
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

b_values = []
for i in range(1, 1001):
    if is_prime(i):
        b_values.append(i)
        b_values.append(-i)
b_values.sort()


max_count = 0
best_a, best_b = 0, 0


for a in range(-1000, 1001):
    for b in b_values:
        n = 0
        while True:
            r = n**2 + a*n + b
            if not is_prime(r):  
                break
            n += 1
        
        if n > max_count:
            max_count = n
            best_a = a
            best_b = b

print(f"Best (a, b) pair: ({best_a}, {best_b})")
print(f"Maximum primes generated: {max_count}")
print(f"Product of a and b: {best_a * best_b}")
