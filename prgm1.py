l=[]
for i in range(1000,4000):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(','.join(l))