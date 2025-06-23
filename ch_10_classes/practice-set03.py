class Demo:
    a = 4

Object = Demo()
print(Object.a) # Prints class attributes 
# because instance attribute is not present

Object.a = 1 # Instance attribute is set
print(Object.a) # Prints class attributes 
# because instance attribute is present

print(Demo.a) # Prints the class attributes

