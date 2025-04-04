num,den=1,1
c=0
for i in range(1,1001):
    on=num
    num=num+2*den
    den+=on
    if(len(str(num))>len(str(den))):
        c=c+1
print(c)