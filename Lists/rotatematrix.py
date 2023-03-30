import numpy as np

myarray = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(myarray)


def rotate(matrix):
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n-layer-1
        for i in range(first, last):
            # save top element
            top = matrix[layer][i]
            # assign left to top
            matrix[layer][i] = matrix[-i-1][layer]
            # assign bottom to left
            matrix[-i-1][layer] = matrix[-layer-1][-i-1]
            # assign right to bottom
            matrix[-layer - 1][-i - 1] = matrix[i][-layer-1]
            # assign top to right
            matrix[i][-layer - 1] = top
    return matrix

print(rotate(myarray))