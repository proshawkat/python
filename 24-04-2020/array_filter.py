import numpy as np

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)

arr = np.array([41, 42, 43, 44])
filter_arr = []
for ele in arr:
    if ele > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

arr = np.array([41, 42, 43, 44])
filter_arr = []
for ele in arr:
    if ele%2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

#Creating Filter Directly From Array
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

#Creating Filter Directly From Array
arr = np.array([41, 42, 43, 44])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)