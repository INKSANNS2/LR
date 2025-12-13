def my_range(start, end, step):
    current = start
    while current < end:
        yield current
        current += step

for i in my_range(1, 6, 0.7):
    print(i)