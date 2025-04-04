def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        p=1
        for i in range(2,n+1):
            p*=i
        return p
    
def cur(n):
    cp=n
    s=0
    while(n>0):
        d=n%10 
        s+=fact(d)
        n=n//10
    if(s==cp):
        return True
    else:
        return False
s=0
for i in range(3,2540170):
    if(cur(i)):
        s+=i
print(s)