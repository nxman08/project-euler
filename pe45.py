import math
def p(n):
    s=(1+math.sqrt(24*n+1))/6
    if(int(s)==s):
        return True
    else:
        return False
    
def h(n):
    s=(1+math.sqrt(8*n+1))/4
    if(int(s)==s):
        return True
    else:
        return False
    
n=286
while True:
    t=n*(n+1)/2
    if(p(t) and h(t)):
        print(t)
        break
    n=n+1