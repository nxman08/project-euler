n=1
c=[]
while (len(c)<1000000):
    c.append(str(n))
    n=n+1

c=''.join(c)

p=1
for i in range(0,6):
    p*=int(c[10**i-1])

print(p)