class MyClass:
    x = 5

p1  = MyClass()
print(p1.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(abc):
        print("Hello my name is "+ abc.name)

p1 = Person("John", 36)
p1.myfunc()