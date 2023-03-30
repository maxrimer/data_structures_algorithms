def openrussiandoll(doll):
    if doll == 1:
        print('All dolls are opened')
    else:
        openrussiandoll(doll-1)


if __name__ == '__main__':
    openrussiandoll(5)