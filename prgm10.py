m= input("enter the input: ")
letters =[letters for letters in m.split(" ")]
print(" ".join(sorted(list(set(letters)))))