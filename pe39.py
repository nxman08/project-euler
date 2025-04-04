m=0
mp=0
for p in range(1,1001):
    cn=0
    for a in range(1,p+1):
        for b in range(1,a+1):
            c=p-a-b
            if(a>b and b>c):
                if(a**2==b**2+c**2):
                    cn=cn+1
    if(cn>m):
        m=cn
        mp=p

print(mp)