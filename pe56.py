import math
m=0
for a in range(1,101):
    for b in range(1,101):
        p=str(a**b)
        s=0
        for c in p:
            s+=int(c)
        if(s>m):
            m=s

print(m)