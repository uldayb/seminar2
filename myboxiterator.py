class MyBoxIterator():
    def __init__(self,L):
        self.L = L
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < len(self.L):
            item = self.L[self.idx]
            self.idx += 1
            return item
        else:
            raise StopIteration
