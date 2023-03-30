def linearsearch(lst, val):
    for i in range(len(lst)):
        if lst[i] == val:
            return i
    return -1


mylist = [1,4,7,3,10]
print(linearsearch(mylist, 5))