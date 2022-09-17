def gen():
    current = 0

    while True:
        yield current
        current += 1


generator = gen()

for _ in range(10):
    print(next(generator))
