class MyNumber:
    def __iter__(xyz):
        xyz.a = 2
        return xyz

    # def __next__(abc):
    #     x = abc.a
    #     abc.a += 1
    #     return x

    def __next__(self):
        if self.a <=20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
myclass = MyNumber()
myiter = iter(myclass)
#
# print(next(myiter))
# print(next(myiter))

for x in myiter:
    print(x)