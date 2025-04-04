lc = set() 
s = 0

for a in range(1, 100):
    for b in range(100, 10000 // a):
        c = a * b
        combined = str(a) + str(b) + str(c)
        
        if len(combined) == 9 and set(combined) == set("123456789"):
            if c not in lc:
                s += c
                lc.add(c)

print(s)
