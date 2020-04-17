thistuple = ("apple", "banana", "cherry")
mytuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# print(thistuple);
# print(thistuple[1]);
# print(thistuple[-1]);
# print(mytuple[2:5]);

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

#print(x)

for i in x:
    print(i)

last = ("apple")
print(type(last))

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

y = thistuple.index(8)

print(x)
print(y)

print(x)

