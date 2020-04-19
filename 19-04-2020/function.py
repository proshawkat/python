def my_function():
    print("Hello from a function")

my_function()

def my_name(fname):
    print(fname + " Ali")

my_name("Shawkat")

def arguments(*kids):
    print("The youngest child is " + kids[2])
    for x in kids:
        print("The youngest child is " + x)

arguments("Emil", "Tobias", "Linus")

def key_arg(child1, child2, child3):
    print("The youngest child is "+ child1)

key_arg(child3="Emil", child2='Tobias', child1='Linus')


def arbitrary_key_arg(**kids):
    print("His last name is "+ kids['mid'])

arbitrary_key_arg(fname="Tobias", lname = "Refsnes", mid="Ali")

def recursion(k):
    if (k > 0):
        result = k + recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example results")
recursion(2)
