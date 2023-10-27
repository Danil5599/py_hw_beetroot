def with_index(iterable, start=0):
    for i, item in zip(range(start, start + len(iterable)), iterable):
        yield i, item

for index, value in with_index(["a", "b", "c"], 2):
    print(index, value)