# x = lambda a : a + 10
x = lambda a, b: a*b
print(x(5, 5))


def myfunc(n):
    return lambda a : a * n

mydouble  = myfunc(2)
mytripler = myfunc(3)

print(mydouble(11))
print(mytripler(11))

