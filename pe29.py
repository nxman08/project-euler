t=[]
for a in range (2,101):
    for b in range(2,101):
        r=a**b
        if(r not in t):
            t.append(r)

print(len(t))