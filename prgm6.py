import math
c = 25
h = 47
store = []
items=[x for x in input("enter the value: ").split(',')]
for d in items:
    store.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
print(','.join(store))