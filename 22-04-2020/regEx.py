import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
y = re.findall("[a-m]", txt)
z = re.search("Portugal", txt)
yy = re.search("i", txt)

if (x):
    print("YES! We have a match!")
else:
    print("No match")

print(y)
print(yy.start())
print(z)

x = re.sub("\s", "9", txt)
print(x)

x = re.sub("\s", "9", txt, 2)
print(x)

x = re.search(r"\bS\w+", txt)
print(x.string)

x = re.search(r"\bS\w+", txt)
print(x.group())