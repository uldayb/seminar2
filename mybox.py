from myboxiterator import MyBoxIterator

class MyBox():
    def __init__(self):
        self.vrbl = list()

    def __len__(self):
        return len(self.vrbl)

    def add(self, item):
        self.vrbl.append(item)

    def remove(self,item):
        assert item in self.vrbl
        idx = self.vrbl.index(item)
        return self.vrbl.pop(idx)

    def __contains__(self, item):
        return item in self.vrbl

    def __iter__(self):
        return MyBoxIterator(self.vrbl)


