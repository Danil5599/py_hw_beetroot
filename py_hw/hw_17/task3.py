class CustomIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

    def __getitem__(self, item):
        return self.data[item]

custom_iter = CustomIterable([1, 2, 3, 4, 5])
for item in custom_iter:
    print(item)

print("Element at index 2:", custom_iter[2])