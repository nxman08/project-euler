import math
def pr(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if(n%i==0):
            return False
    return True

k=1
pc=0
tc=1
while 1:
    br=(2*k+1)**2
    bl=br-2*k
    tl=bl-2*k
    tr=tl-2*k
    c=[br,bl,tl,tr]
    for i in c:
        if(pr(i)):
            pc+=1
    tc+=4
    pp=pc/tc*100
    if(pp<=10):
        break
    k=k+1

k=2*k+1
print(k)