import numpy as np

twodarray = np.array([[11,15,10,6], [10,14,11,5], [12,17,12,8], [15,18,14,9]])
print(twodarray)


def searchelement2Darray(array, val):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == val:
                return 'The element is found at index ' + str(i) + ' ' + str(j)
    return 'The element is not found'


print(searchelement2Darray(twodarray, 14))