from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1,  0.3, 0.0, 0.6], size=(100))
x = random.choice([3, 5, 7, 9], p=[0.1,  0.3, 0.0, 0.6], size=(3, 100))
print(x)