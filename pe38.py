def pan(n):
    return len(str(n))==9 and set(str(n))==set("123456789")

lp=0

for i in range(1,10000):
    m=1
    s=''
    while(len(s)<9):
        s=s+str(m*i)
        m=m+1
    if(pan(s)):
        lp=max(lp,int(s))

print(lp)