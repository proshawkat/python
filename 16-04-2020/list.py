thislist = ['apple', 'banana', 'cherry']
thislist[0] = 'blackcurrant'
thislist.append('orange')
thislist.insert(1, 'orange')
thislist.remove('orange')
thislist.pop(1)
del thislist[0]
# thislist.clear()
mylist = list(thislist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2

# another way
for x in list2:
    list1.append(x)

print(list1)

thislist_2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)
print('dd '+ thislist[-1])
print(mylist)
print(thislist_2[2:5])
print(thislist_2[-4:-1])

for x in thislist_2:
    print(x)

if "apple" in thislist_2:
    print("Yes, 'apple' is in the fruits list")

print(list3)