class Queue:
    def __init__(self):
        self.items = UnsortedList()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return self.items.is_empty()

    def size(self):
        return self.items.size()