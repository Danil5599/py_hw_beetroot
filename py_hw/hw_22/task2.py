class Stack:
    def __init__(self):
        self.items = UnsortedList()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items.is_empty()

    def size(self):
        return self.items.size()