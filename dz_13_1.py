number = int(input("Введите число: "))


def fibonacci_gen():
    """Генератор последовательности Фибоначчи"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fibonacci = fibonacci_gen()
for i in range(number):
    print(next(fibonacci))
