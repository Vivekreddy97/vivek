from operator import itemgetter
b=[]
while True:
    f=input("enter the data: ")
    if not f:
        break
    b.append(tuple(f.split(',')))

print(b,b.sort(key=(itemgetter(0,1,2))))