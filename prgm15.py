a = input(" enter the value: ")

v1 = int("%s" % a)
v2 = int("%s%s" % (a, a))
v3 = int("%s%s%s" % (a, a, a))
v4 = int("%s%s%s%s" % (a, a, a, a))
g = v1 + v2 + v3 + v4
print(g)
