import math
def div(s):
    d=0
    for i in range(1,int(math.sqrt(s))):
        if(s%i==0):
          d+=2
    if math.sqrt(s)==int(math.sqrt(s)):
        d=d-1
    return d

c=1
s=0
while True:
    s+=c
    if(div(s)>500):
        print(s)
        break
    c+=1