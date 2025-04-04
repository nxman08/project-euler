import math

s=str(int(math.pow(2,1000)))

p=0
for i in s:
    p+=int(i)

print(p)