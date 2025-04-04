def tr(n):
    for i in range(1,n+1):
        s=(i*(i+1))/2
        if(s==n):
            return True
    return False


f=open ("/Users/namanagarwal/VS code/project euler/0042_words.txt",'r')
w=f.read().strip().replace('"','').split(',')

cnt=0
for i in range(0,len(w)):
    c=w[i].lower()
    s=0
    for char in c:
        s=s+ord(char)-96
    if(tr(s)):
        cnt=cnt+1

print(cnt)