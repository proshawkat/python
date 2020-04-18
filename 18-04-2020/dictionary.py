thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

#print(thisdict['year']);
#print(thisdict.get('year'));

#for x,y in thisdict.values():
for x,y in thisdict.items():
    print(x,y)
# thisdict.pop("model")
# del thisdict['model']

# thisdict.popitem()

# mydict = thisdict.copy()
mydict = dict(thisdict)

print(mydict)
print(thisdict)
print(len(thisdict))