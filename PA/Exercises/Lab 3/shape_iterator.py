class ShapeSortIterator:
    def __init__(self, container, op):
        self.container = container
        self.index = 0
        self.cmp = op
    def __iter__(self):
        self.index = 0
        for obj in self.container:
            obj.lessthan = self.cmp.__get__(obj, type(obj))
        self.container.sort()
        return self
    def __next__(self):
        while True:
            if self.index == len(self.container):
                raise StopIteration
            res = self.container[self.index]
            self.index += 1
            return res
    def set_compare(self, op):
        self.cmp = op
