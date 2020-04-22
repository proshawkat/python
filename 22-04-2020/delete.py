import os

if os.path.exists("delete.txt"):
    os.remove("delete.txt")
    print("The file successfully has been deleted")
else:
    print("The file does not exist")
