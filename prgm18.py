import re

values = []
data = [a for a in input("enter the password: ").split(',')]
for a in data:
    if len(a) < 6 or len(a) > 12:
        continue
    else:
        pass
    if not re.search("[a-z]", a):
        continue

    elif not re.search("[0-9]", a):
        continue

    elif not re.search("[A-Z]", a):
        continue

    elif not re.search("[$#@]", a):
        continue
    elif not re.search("[/s]", a):
        continue
    else:
        pass
    values.append(a)

print(','.join(values))
