def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
np=1
dp=1
for a in range (10,100):
    for b in range (a+1,100):
        sa,sb=str(a),str(b)
        com=set(sa) & set(sb)

        for d in com:
            if(int(d)==0):
                continue
            na=int(sa.replace(d,"",1))
            nb=int(sb.replace(d,"",1))

            if(nb==0):
                continue
            
            if(na*b==nb*a):
                np*=a
                dp*=b

g= gcd(np,dp)
d=dp//g

print(d)