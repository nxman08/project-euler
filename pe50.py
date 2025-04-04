import math

def pr(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
"""
m=0
s=0
n=2
while s+n<1000000:
    if(pr(n)):
        s=s+n
        if(pr(s)):
            m=max(m,s)
    n=n+1
"""

r=[]
for n in range(2,101):
    s=0
    m=0
    if(pr(n)):
        while s+n<1000000:
            if(pr(n)):
               s=s+n
               if(pr(s)):
                   m=max(s,m)
            n=n+1
        r.append(m)

print(max(r))