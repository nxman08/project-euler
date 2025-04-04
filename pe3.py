import math
def prime(n):
    out=[]
    while n%2==0:
        out.append(2)
        n/=2
    
    for i in range(3,int(math.sqrt(n)+1),2):
        while n%i==0:
            out.append(i)
            n=n/i

    if n>2:
        out.append(int(n))
    return out

print(max(prime(600851475143)))
