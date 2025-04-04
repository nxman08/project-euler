from itertools import permutations as p

def div(n):
    primes = [2, 3, 5, 7, 11, 13, 17]
    
    for i in range(7):
        if int(n[i+1:i+4]) % primes[i] != 0:
            return False
    return True

s=0
for i in p('1234567890'):
    num="".join(i)
    if(div(num)):
        s+=int(num)
print(s)