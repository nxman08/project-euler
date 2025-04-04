import math
def pr(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False  
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def ltr(n):
    n=str(n)
    for i in range(0,len(n)):
        if(pr(int(n[i:]))):
            continue
        else:
            return False
    return True


def rtr(n):
    n=str(n)
    for i in range(len(n),0,-1):
        if(pr(int(n[:i]))):
            continue
        else:
            return False
    return True

c=0
n=11
r=[]
while(c!=11):
    if(rtr(n) and ltr(n)):
        r.append(n)
        c=c+1
    n=n+2

print(sum(r))