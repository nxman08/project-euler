import math 
def prime(n):
    if n%2==0:
        return False
    for i in range (2,int(math.sqrt(n))+1):
        if(n%i==0):
            return False
    return True

n=1
pr=1
while (pr<10001):
    n+=1
    if (prime(n)):
        pr+=1

print(n)