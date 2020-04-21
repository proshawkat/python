import datetime as dt

x = dt.datetime.now()
y = dt.datetime(2020, 5, 17)

print(x)
print(x.year)
print(x.strftime("%A"))
print(x.strftime("%W"))
print(y)