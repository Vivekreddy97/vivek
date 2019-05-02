t= input("enter data :")
m= {"DIGITS":0,"LETTERS":0}
for c in t:
    if c.isdigit():
        m["DIGITS"]+=1
    elif c.isalpha():
        m["LETTERS"]+=1
    else:
        pass
print("ALPHABETS",m["LETTERS"])
print("DIGITS",m["DIGITS"])