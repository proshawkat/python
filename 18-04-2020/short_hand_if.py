a = int(input("Enter your number "))
b = 33
c = 500
x = 41
if a > b: print("a is greater than b")

print("A") if a > b else print("B")

print("A") if a > b else print("=") if a==b else print("B")

if a > b and c > a:
  print("Both conditions are True")

if a > b or a > c:
      print("At least one of the conditions is True")

#Nested If
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

