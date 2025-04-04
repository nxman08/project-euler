f = open("/Users/namanagarwal/VS code/project euler/name.txt", "r")
d=f.read()
f.close()


d=d.replace('"','')
name=d.split(',')
name.sort()

def nw(n):
    s=0
    for i in n:
        s+=(ord(i)-64)
    return s

def ns(name, index):
    return nw(name[index])*(index+1)


sum=0
for i in range(0,len(name)):
    sum+=ns(name,i)

print(sum)