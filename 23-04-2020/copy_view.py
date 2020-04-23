import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)

print("View")
# View
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

# make changes in the view
print("make changes in the view")
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31
print(arr)
print(x)

# Check if Array Owns it's Data
print("Check if Array Owns it's Data")
arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x)
print(y.base)