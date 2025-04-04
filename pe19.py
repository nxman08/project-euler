import datetime

c = 0
for i in range(1901, 2001):  
    for j in range(1, 13):  
        if 'Sunday' == datetime.date(i, j, 1).strftime('%A'):  
            c += 1

print(c)  
