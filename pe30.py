def s(n):
    d=[]
    for i in str(n):
        d.append(int(i)**5)
    return sum(d)

r=[]
for i in range(2,354295):
    if(s(i)==i):
        r.append(i)
print(sum(r))