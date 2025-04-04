import math
o=[]
for n in range(1,101):
    for r in range(1,n+1):
        c=math.comb(n,r)
        if(c>1000000):
            o.append(c)

print(len(o))