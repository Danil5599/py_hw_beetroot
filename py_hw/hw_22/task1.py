class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None


class UnsortedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def append(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def index(self, item):
        current = self.head
        index = 0
        while current:
            if current.data == item:
                return index
            current = current.next
            index += 1
        raise ValueError(f"{item} not in list")

    def pop(self, index=None):
        if self.is_empty():
            raise IndexError("pop from empty list")
        if index is None:
            index = self.size() - 1

        current = self.head
        previous = None
        pos = 0
        while pos != index:
            previous = current
            current = current.next
            pos += 1

        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

        return current.data

    def insert(self, index, item):
        if index > self.size():
            raise IndexError("list index out of range")

        temp = Node(item)
        current = self.head
        previous = None
        pos = 0
        while pos != index:
            previous = current
            current = current.next
            pos += 1

        if previous is None:
            temp.next = self.head
            self.head = temp
        else:
            temp.next = current
            previous.next = temp

    def slice(self, start, stop):
        if start > self.size() or stop > self.size() or start > stop:
            raise IndexError("list index out of range")

        current = self.head
        index = 0
        result = UnsortedList()
        while current and index < stop:
            if index >= start:
                result.append(current.data)
            current = current.next
            index += 1
        return result

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count