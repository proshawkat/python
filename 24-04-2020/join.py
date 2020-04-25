import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)
arrs = np.stack((arr1, arr2), axis=1)
print(arrs)
arrh = np.hstack((arr1, arr2))
print(arrh)
arrv = np.vstack((arr1, arr2))
print(arrv)
arrd = np.dstack((arr1, arr2))
print(arrd)
