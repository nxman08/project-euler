s=0
a=0
b=1
c=a+b
while(c<=4000000):
    if(c%2==0):
        s+=c
    a=b
    b=c
    c=a+b

print(s)