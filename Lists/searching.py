mylist = [10,20,30,40,50,60,70,80,90]

# if 50 in mylist:
#     print(mylist.index(50))
# else:
#     print('No such value in the list')


def searchinglist(list, value):
    for i in list:
        if i == value:
            return list.index(i)
    return 'No such element'

print(searchinglist(mylist, 20))