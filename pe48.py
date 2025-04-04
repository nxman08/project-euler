s=0
for i in range(1,1001):
    s+=i**i

s=str(s)
l=len(s)
print(s[l-10:])