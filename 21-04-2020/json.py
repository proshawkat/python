#!/usr/bin/python
import simplejson

x = '{"name":"John", "age":30, "city":"New York"}'
y = simplejson.dumps(x)
print(y)

print(simplejson.dumps({"name": "John", "age": 30}))
print(simplejson.dumps(["apple", "bananas"]))
print(simplejson.dumps(("apple", "bananas")))
print(simplejson.dumps("hello"))
print(simplejson.dumps(42))
print(simplejson.dumps(31.76))
print(simplejson.dumps(True))
print(simplejson.dumps(False))
print(simplejson.dumps(None))

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(simplejson.dumps(x, indent=4, separators=(". ", " = ")))