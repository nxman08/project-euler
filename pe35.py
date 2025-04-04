import math
def pr(n):
    c=0
    for i in range (2,int(math.sqrt(n))+1):
        if(n%i==0):
            return False
    return True

def rt(n):
    n=str(n)
    r=[]
    for i in range(len(n)):
        r.append(int(n[i:]+n[:i]))
    return r

count=0
for i in range(2,1000000):
    if(pr(i)):
        r=rt(i)
        b=[]
        for n in r:
            if(pr(n)):
                b.append(1)
            else:
                b.append(0)
        if(0 in b):
            continue
        else:
            count=count+1

print(count)