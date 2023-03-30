import math


def binarysearch(srtlst, val):
    left = 0
    right = len(srtlst) - 1
    middle = math.floor((left + right) / 2)

    while not(srtlst[middle] == val) and left <= right:
        if srtlst[middle] > val:
            right = middle - 1
        else:
            left = middle + 1
        middle = math.floor((left + right) / 2)

    if srtlst[middle] == val:
        return middle
    return -1


mylist = [1, 3, 5, 7, 9, 11, 15, 20, 25, 27]
print(binarysearch(mylist, 100))