import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
  print(x)

# Iterating 2-D Arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)

for x in arr:
  for y in x:
      print(y)

# Iterating 3-D Arrays
print("Iterating 3-D Arrays")
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)

for x in arr:
    for y in x:
      for z in y:
          print(z)

# Iterating Arrays Using nditer()
print("Iterating Arrays Using nditer()")
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)

# Iterating With Different Step Size
print("Iterating With Different Step Size")
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)

#Enumerated Iteration Using ndenumerate()
print("Enumerated Iteration Using ndenumerate()")
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)