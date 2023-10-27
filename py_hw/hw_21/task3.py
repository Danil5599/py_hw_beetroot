class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def get_from_stack(self, e):
        if e in self.items:
            self.items.remove(e)
            return e
        else:
            raise ValueError(f"{e} not found in the stack")


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def get_from_queue(self, e):
        if e in self.items:
            self.items.remove(e)
            return e
        else:
            raise ValueError(f"{e} not found in the queue")


def extend_stack_for_search():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.get_from_stack(2))
    try:
        print(s.get_from_stack(4))
    except ValueError as e:
        print(e)


def extend_queue_for_search():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.get_from_queue(2))
    try:
        print(q.get_from_queue(4))
    except ValueError as e:
        print(e)


extend_stack_for_search()
extend_queue_for_search()
