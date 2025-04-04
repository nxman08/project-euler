import math
def pr(n):
    if(n==1):
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return False
    return True

def fac(n):
    c=0
    i=2
    while n>1:
        if(n%i==0):
            c=c+1
            while n%i==0:
                n//=i
        i=i+1
    return c==4    

n=100000
while True:
    if(fac(n) and fac(n+1) and fac(n+2) and fac(n+3)):
        print(n)
        break
    n=n+1