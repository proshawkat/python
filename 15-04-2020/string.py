a = "Hello, World! "
b = "Hello World!"
txt = "The rain in Spain stays mainly in the plain"
c = "ain" in txt

age = 36
my = "My name is John and I am {}"

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {2} pieces of item {0} for {1} dollars."

print(a[1])
print(b[2:4]) #Get the characters from position 2 to position 4
print(b[-5:-3]) #Get the characters from position 5 to position 1, starting the count from the end of the string
print(len(a))
print(a.strip())
print(a.lower())
print(a.upper())
print(a.replace("H", "J"))
print(a.split(",")[0])
print(c)
print(my.format(age))
print(myorder.format(quantity, itemno, price))
print(c.lstrip())
