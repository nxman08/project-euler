import math
ab=[]
for i in range(1,28124):
    s=[1]
    for j in range(2,int(math.sqrt(i))+1):
        if(i%j==0):
            s.append(j)
            if(i//j!=j):
                s.append(i//j)

    if(sum(s)>i):
        ab.append(i)
ab=set(ab)
ns=[]
for i in range(1,28124):
    c=0
    for j in range(1,i):
        s1=j
        s2=i-j
        if(s1 in ab and s2 in ab):
            c=1
            break
    if(c==0):
        ns.append(i)

print(sum(ns))