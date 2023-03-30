# Accesing elements in 2D Arrays
import numpy as np


twodarray = np.array([[11,15,10,6], [10,14,11,5], [12,17,12,8], [15,18,14,9]])
print(twodarray)


def getelement(array, rowindex, colindex):
    if rowindex >= len(array) or colindex >= len(array[0]):
        return 'Indexes out of range'
    return array[rowindex][colindex]


print(getelement(twodarray, 2, 4))

