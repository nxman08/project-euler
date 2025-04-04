from itertools import permutations
d='0123456789'
p=list(permutations(d))

for i in p[999999]:
    print(i,end="")