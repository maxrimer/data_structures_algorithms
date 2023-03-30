import numpy as np

twodarray = np.array([[11,15,10,6], [10,14,11,5], [12,17,12,8], [15,18,14,9]])
print(twodarray)


def traversing2Darray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])


traversing2Darray(twodarray)