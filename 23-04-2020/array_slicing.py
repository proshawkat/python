import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])
print(arr[4:])
print(arr[:4])

#negative
print(arr[-3:-1])
# step
print(arr[0:5:2])
# every element
print(arr[::2])

# slicing 2-D arrays
print("2-D array")
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, :4])
print(arr[0:2, 2])
print(arr[0:2, 1:4])

for row in arr:
    for col in row:
        print(col, end=" ")
    print()