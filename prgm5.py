class InputOutString(object):
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s=("Enter the string")
    def printString(self):
       print(self.s.upper())

k=InputOutString()
k.getString()
k.printString()
