import math
def sum(n):
    c=1
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            c+=i
            if(i!=n//i):
                c+=n//i
    return c

p=0
for i in range(1,10001):
    j=sum(i)
    if(j>i and sum(j)==i):
        p+=i+j

print(p)