def poweroftwo(n):
    return 2**n


def poweroftworec(n):
    if n == 0:
        return 1
    else:
        power = poweroftworec(n-1)
        return power * 2


def poweroftwoiter(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i += 1
    return power


if __name__ == '__main__':
    print(poweroftwoiter(5))
    print(poweroftworec(5))

# сначала 1
# потом от poweroftworec(1) возвращается 2
# потом от poweroftworec(2) возвращается 4