def in_range(start, end=None, step=1):
    if end is None:
        end = start
        start = 0

    while start < end:
        yield start
        start += step

for i in in_range(3, 7):
    print(i)