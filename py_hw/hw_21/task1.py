class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def reverse_sequence(sequence):
    s = Stack()
    for char in sequence:
        s.push(char)
    reversed_seq = ""
    while not s.is_empty():
        reversed_seq += s.pop()
    return reversed_seq


seq = input("Enter a sequence: ")
print("Reversed sequence:", reverse_sequence(seq))