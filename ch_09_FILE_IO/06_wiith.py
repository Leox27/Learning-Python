# Open and clise the file "with" statement


file = open("file.txt")
print(file.read())
file.close()

# The same can be written using with statementts like this:
with open ("file.txt") as f:
    file.read()

# you dont have to close the file