def bi(n):
    return int(bin(n)[2:])

def rev(n):
    n=str(n)
    if(n==n[::-1]):
        return True
    else:
        return False

p=[]
for i in range(1,1000001):
    if(rev(i) and rev(bi(i))):
        p.append(i)

print(sum(p))