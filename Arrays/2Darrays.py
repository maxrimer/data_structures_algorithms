import numpy as np

twodarray = np.array([[11,15,10,6], [10,14,11,5], [12,17,12,8], [15,18,14,9]])
print(twodarray)

newarray = np.insert(twodarray, 4, [[1,2,3,4]], axis=1)
print(newarray)

# newarray = np.append(twodarray, [[6,7,8,9]], axis=0)
# print(newarray)