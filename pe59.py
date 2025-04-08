from itertools import product
f=open ("/Users/namanagarwal/VS code/project euler/0059_cipher.txt",'r')
w=f.read()
f.close()
data = list(map(int, w.strip().split(',')))

for c1 in range(ord('a'),ord('z')+1):
    for c2 in range(ord('a'),ord('z')+1):
        for c3 in range(ord('a'),ord('z')+1):
            key=[c1,c2,c3]
            d=[]
            for i in range(len(data)):
                ec=data[i]
                kc=key[i%3]
                dc=ec^kc
                d.append(dc)
            text = ''.join(map(chr, d))    

            if ('the' in text and 'is' in text and 'and' in text and 'be' in text and 'by' in text and 'from' in text):
                print("Key found",''.join(map(chr, key)))
                print("Decrypted Message",text,"\n..")
                print(" Sum of ASCII values:", sum(d))
                break

