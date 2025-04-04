def palindrome(n):
    s=str(n)
    if(s==s[::-1]):
        return True
l=0
for i in range(999,100,-1):
    for j in range(999,100,-1):
        if(i*j>l):
            if(palindrome(i*j)):
                l=(i*j)

print(l)