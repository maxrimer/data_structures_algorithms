def factorial(n):
    assert n >= 0 and int(n) == n, 'Number must be positive integeer or 0'
    if n in (0,1):
        return 1
    else:
        return n * factorial(n-1)


def fibonacci(num):
    assert num >= 0 and int(num) == num, 'Number must be positive integeer or 0'
    if num in (0, 1):
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)


if __name__ == '__main__':
    print(fibonacci(6))