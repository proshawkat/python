try:
    print(x)
except NameError:
    print("1 Variable x is not defined")
except:
    print("1 An exception occurred")
else:
    print("1 Nothing went wrong")

# 2
try:
    print("2 Hello")
except:
    print("2 An exception occurred")
else:
    print("2 Nothing went wrong")

# 3
try:
    print(x)
except:
    print("3 Something went wrong")
finally:
    print("3 The 'try except' is finished")

#4
try:
    f = open("demofile.txt")
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()

#5
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")

#6
x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")