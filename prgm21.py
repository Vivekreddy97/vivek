import  math
pos=[0,0]
while True:
    k = input("enter data: ")
    if not k :
        break
    noddng = k.split(" ")
    direction = noddng[0]
    steps = int(noddng[1])
    if direction=="UP":
        pos[0] += steps
    elif direction == "DOWN":
        pos[0] -= steps
    elif direction == "LEFT":
        pos[1] += steps
    elif direction == "RIGHT":
        pos[1] -= steps
    else:
        pass
print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))