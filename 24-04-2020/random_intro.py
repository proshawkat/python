from numpy import random
x = random.randint(100)
x = random.rand()
x = random.randint(100, size=(5))
x = random.randint(100, size=(3, 5))
x = random.rand(5)
x = random.rand(3, 5)

# generate random number from array
x = random.choice([3, 5, 7, 9])
x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)