import numpy as np
arr = np.array([1, 2, 3, 4, 5])
arr1 = np.array((1, 2, 3, 4, 5))
print(arr)
print(arr1)
print(type(arr))

# 2-D array
arr = np.array([[1, 2, 3,], [4, 5, 6]])
print(arr)

# 3-D array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)

# check
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a)
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Higher dimentional array
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print("Number of dimension : ", arr.ndim)