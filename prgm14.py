h= input( "enter data : ")
d={"UPPER" :0, "LOWER":0}
for a in h:
    if a.isupper():
        d["UPPER"]+=1
    elif a.islower():
        d["LOWER"]+=1
    else:
        pass
print ("UPPER CASE", d["UPPER"])
print ("LOWER CASE", d["LOWER"])