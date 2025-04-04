import math
def pr(n):
    if(n==1):
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return False
    return True

def f(n):
    for i in range(1,n):
        if(pr(i) and int(math.sqrt((n-i)/2))==math.sqrt((n-i)/2)):
            return False
    return True

for i in range(35,1000000000,2):
    if(not pr(i)):
        if(f(i)):
            print(i)
            break