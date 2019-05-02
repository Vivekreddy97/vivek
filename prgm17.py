netamount=0
while True:
    s = input("enter transaction: ")
    if not s:
        break
    values = s.split(" ")
    type = values[0]
    amount = int(values[1])
    if type == "D":
        netamount+=amount
    elif type== "W":
        netamount-="W"
    else:
        pass
    s = input("want to continue (Y for yes) : ")
    if not (s[0] == "Y" or s[0] == "y"):
        break
print("NET AMOUNT: ",netamount)

