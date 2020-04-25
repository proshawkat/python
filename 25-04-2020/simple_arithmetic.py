import numpy as np

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.add(arr2, arr1)
newarr = np.subtract(arr2, arr1)
newarr = np.multiply(arr2, arr1)
newarr = np.divide(arr2, arr1)
newarr = np.power(arr2, arr1)
newarr = np.mod(arr2, arr1)
newarr = np.remainder(arr2, arr1)
newarr = np.divmod(arr2, arr1)
newarr = np.absolute(arr2, arr1)

print(newarr)