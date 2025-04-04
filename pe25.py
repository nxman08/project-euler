cnt=2
a=1
b=1
while True:
    cnt+=1
    c=a+b
    if(len(str(c))>=1000):
        break
    a=b
    b=c
    
print(cnt)