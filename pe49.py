import math
from itertools import permutations

def pr(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if(n%i==0):
            return False
    return True

p=[]
for i in range (1000,10000):
    if (pr(i)):
        p.append(i)

p=set(p)

for i in range(1000,10000):
    for n in p:
        if((n+i) in p and (n+i+i) in p):
            perm=list(permutations(str(n)))
            if(tuple(str((n+i))) in perm and tuple(str((n+i+i))) in perm):
                print(str(n)+str(n+i)+str(n+i+i))
                break