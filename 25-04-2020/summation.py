import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 2, 3])
newarr = np.sum([arr1, arr2])
newarr = np.sum([arr1, arr2], axis=1)
newarr = np.cumsum(arr1)
newarr = np.cumsum([arr1, arr2], axis=1)

print(newarr)