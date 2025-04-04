def same(a,b,c,d,e,f):
    a,b,c,d,e,f= str(a),str(b),str(c),str(d),str(e),str(f)
    a,b,c,d,e,f=list(a),list(b),list(c),list(d),list(e),list(f)
    a.sort()
    b.sort()
    c.sort()
    d.sort()
    e.sort()
    f.sort()
    if(a==b==c==d==e==f):
        return True
    else:
        return False


n=1
b=False
while not b:
    n2=2*n
    n3=3*n
    n4=4*n
    n5=5*n
    n6=6*n
    b=same(n,n2,n3,n4,n5,n6)
    n=n+1

print(n-1)