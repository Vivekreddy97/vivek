values= input("enter the values : ")
dimensions=[int(x) for  x in values.split(',')]
rowNum = dimensions[0]
colNum = dimensions[1]
multilist = []
for row in range(rowNum):
    multilist.append([0 for col in range(colNum)])
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row*col
print(multilist)