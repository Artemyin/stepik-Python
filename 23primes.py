def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result = result * i
    return result


def is_prime(x):
    result = (factorial(x-1) + 1) % x
    return bool(result == 0)


def primes():
    i = 2
    while True:
        if is_prime(i) is True:
            yield i
        i = i + 1




import itertools

print(list(itertools.takewhile(lambda x: x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
