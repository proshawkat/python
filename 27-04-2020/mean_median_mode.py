import numpy as np
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = np.mean(speed)
print(x)

x = np.median(speed)
print(x)

# If there are two numbers in the middle, divide the sum of those numbers by two. (86 + 87) / 2 = 86.5
speed = [99,86,87,88,111,86,87,94,78,77,85,86]

x = np.median(speed)
print(x)


# The Mode value is the value that appears the most number of times:
x = stats.mode(speed)
print(x)
