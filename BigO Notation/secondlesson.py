# def findbiggestnumber(arr):
#     if len(arr) == 1:
#         return arr[0]
#     return max(arr[-1], findbiggestnumber(arr[0:len(arr) - 1]))
#
#
# print(findbiggestnumber([1,3,8,4,2,9,16,5]))


def findbiggestnumberiter(arr):
    biggest_num = arr[0]
    for item in arr[1:]:
        if item > biggest_num:
            biggest_num = item
    return biggest_num


print(findbiggestnumberiter([1,3,8,4,2,9,16,5,30,3]))