def count_collatz(n):
    if n==1:
        return 1
    if n%2==0:
        n=n//2
        return 1+ count_collatz(n)
    if n%2==1:
        n=3*n+1
        return 1+ count_collatz(n)

ml=0
mln=0
for i in range(1,1000000):
    l=count_collatz(i)
    if(l>ml):
        ml=l
        mln=i

print(mln)