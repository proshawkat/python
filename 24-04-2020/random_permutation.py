from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)

arr = np.array([1, 2, 3, 4, 6])
print(random.permutation(arr))