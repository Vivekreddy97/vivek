class iterator(object):
    def __init__(self, n):
        super(iterator, self).__init__()
        self.n = n

    def div7(self):
        for i in range(0, self.n):
            if i % 7 == 0:
                yield i


for c in iterator(100).div7():
    print(c)
