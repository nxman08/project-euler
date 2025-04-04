import math
def prime(n):
    if n%2==0:
        return False
    for i in range(3,int(math.sqrt(n))+1):
        if(n%i==0):
            return False
    return True

a=[2]

for i in range (3,2000000,2):
    if(prime(i)):
        a.append(i)

print(sum(a))