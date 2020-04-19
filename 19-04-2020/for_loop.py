fruits = ['apple', 'banana', 'chery']
for x in fruits:
    if x == 'banana':
        continue
    print(x)

# range
for x in range(2,10,3):
    print(x)

else:
    print("Finally finished!")

#nested loops
adj = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'cherry']

for x in adj:
    for y in fruits:
        print(x, y)

#pass statement
for x in [0,1,2]:
    pass