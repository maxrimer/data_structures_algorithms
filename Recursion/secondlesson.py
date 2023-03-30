def firstMethod():
    secondMethod()
    print('I am the first method')


def secondMethod():
    thirdMethod()
    print('I am the second method')


def thirdMethod():
    fourthMethod()
    print('I am the third method')


def fourthMethod():
    print('I am the fourth method')


def recursivemethod(n):
    if n < 1:
        print(f'{n} is less than 1')
    else:
        recursivemethod(n - 1)
        print(n)


if __name__ == '__main__':
    recursivemethod(4)
