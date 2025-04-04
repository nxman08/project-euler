cnt=1
for a in range(201):
    for b in range(101-(a//2)):
        for c in range(41-(2*b+a)//5):
            for d in range(21-(5*c+2*b+a)//10):
                for e in range(11-(10*d+5*c+2*b+a)//20):
                    for f in range(5-(20*e+10*d+5*c+2*b+a)//50):
                        for g in range(3-(50*f+20*e+10*d+5*c+2*b+a)//100):
                            if(a+2*b+5*c+10*d+20*e+50*f+100*g==200):
                                cnt+=1
print(cnt)