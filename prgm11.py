data=[]
items =[a for a in input("enter: ").split(',')]
for x in items:
    b = int(x,2)
    if not b%5:
        data.append(x)
print(','.join(data))