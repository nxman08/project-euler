def cycle_length(d):
    remainders = {} 
    numerator = 1
    position = 0

    while numerator != 0:
        numerator = numerator % d 
        if numerator in remainders:
            return position - remainders[numerator]  
        remainders[numerator] = position  
        numerator *= 10  
        position += 1

    return 0  


max_length = 0
best_d = 0

for d in range(2, 1000):  
    length = cycle_length(d)
    if length > max_length:
        max_length = length
        best_d = d

print(best_d)  
