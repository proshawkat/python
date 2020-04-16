x = "awesome"

def myfunc():
    print("Python is "+ x)

def secfunc():
    x = "fantastic"
    print("Python is "+ x)

def thirdfunc():
    global y
    y = "nice"

myfunc()

secfunc()

thirdfunc()
print("Python is "+ y)

print("Python is "+ x)
