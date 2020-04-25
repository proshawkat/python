import numpy as np
from math import log

arr = np.arange(1, 10)

print("Log 2")
print(np.log2(arr))

print("Log 10")
print(np.log10(arr))

print("Natural Log")
print(np.log(arr))

print("Log at any base")
nplog = np.frompyfunc(log, 2, 1)
print(nplog(2, 3))