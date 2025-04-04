s=1
for i in range(1,101):
    s=s*i
s=str(s)
m=0
for i in s:
    m+=int(i)
print(m)