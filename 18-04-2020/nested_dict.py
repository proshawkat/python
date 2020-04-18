# myfamily = {
#     "child1" : {
#         "name": "Emil",
#         "year": 2004
#     },
#     "child2": {
#         "name" : "Tobias",
#         "year" : 2007
#     },
#     "child3" : {
#         "name" : "Linus",
#         "year" : 2011
#     }
# }

# another way

child1 = {
    "name": "Emil",
    "year": 2004
}
child2 =  {
    "name" : "Tobias",
    "year" : 2007
}
child3 = {
    "name" : "Linus",
    "year" : 2011
}

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3,
}

print(myfamily['child1']['name'])

thisdict = dict(brand="Ford", model= "Mustang", year=1964)
print(thisdict);