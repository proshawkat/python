cars = ["Ford", "Volbo", "BMW"]
# print(len(cars))

# for x in cars:
#     print(x)

cars.append("Honda")
# print(cars)

# sort()
cars.sort(reverse=True)
print(cars)


def myfunction(e):
    return len(e)
cars.sort(key=myfunction)
print(cars)