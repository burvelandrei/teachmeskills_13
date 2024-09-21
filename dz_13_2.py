number = int(input("Введите число: "))

def sequence(number: int):
    a = 1
    while a <= number:
        yield a
        a += 1


def infinite_sequence(number: int):
    for _ in range(100000):
        seq = sequence(number)
        for j in seq:
            yield j

print(*infinite_sequence(number), sep="-")