import math

def pr(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def count(n):
    n = str(n)
    d = {i: n.count(str(i)) for i in range(0, 10)} 
    return d

for i in range(1, 1000000):
    d = count(i)
    m = max(d, key=d.get)  
    
    s = str(i).replace(str(m), '*') 
    
    c = 0  
    for j in range(0, 10):  
        r = s.replace("*", str(j))
        
      
        if r[0] == '0':
            continue
        
        if pr(int(r)):  
            c += 1
    
    if c == 8: 
        print(i)
        break