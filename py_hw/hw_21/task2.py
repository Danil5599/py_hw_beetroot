class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

def is_balanced(sequence):
    s = Stack()
    for char in sequence:
        if char in "([{":
            s.push(char)
        else:
            if s.is_empty():
                return False
            top = s.pop()
            if char == ")" and top != "(":
                return False
            elif char == "]" and top != "[":
                return False
            elif char == "}" and top != "{":
                return False
    return s.is_empty()

seq = input("Enter a sequence: ")
print("Is the sequence balanced?", is_balanced(seq))
