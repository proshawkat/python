y = 200
def myfunc():
    x = 300
    global y
    y = 500
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

print(y)