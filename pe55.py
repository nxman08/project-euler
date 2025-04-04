def pal(n):
    n=str(n)
    if(n==n[::-1]):
        return True
    return False

def ly(n):
    c=0
    while(c<=50):
        n+=int(str(n)[::-1])
        if(pal(n)):
            return False
        c=c+1
    return True

c=0
for i in range(1,10001):
    if(ly(i)):
        c=c+1
    
print(c)