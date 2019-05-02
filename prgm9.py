data=[]
while True:
    m = input("enter: ")
    if m:
        data.append(m.upper())
    else:
        break;
for sentence in data:
    print(sentence)