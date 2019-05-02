data =[]
for  n in range(1000,4000):
    t= str(n)
    if (int(t[0])%2==0) and (int(t[1])%2==0) and (int(t[2])%2==0) and(int(t[3])%2==0):
        data.append(t)
print(','.join(data))