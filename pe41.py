import math
def pan(n):
    l=len(str(n))
    for i in range(1,l+1):
        if(str(i) in str(n)):
            continue
        else:
            return False
    return True

def pr(n):
    for i in range(2, int(math.sqrt(n))+1):
        if(n%i==0):
            return False
    return True

m=0

for i in range(7654321,1234566,-2):
    if(pr(i) and pan(i) and i>m):
        m=i
        break

print(m)