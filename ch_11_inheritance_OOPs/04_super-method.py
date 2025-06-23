class Employee:
    def __init__(self):
        print("Constructor is Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        # super().__init__()
        print("Constructor is Programmer")
    b =2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor is Manager")
    c = 3

# o = Employee()
# print(o.a) # print the attribute

# o = Programmer()
# print(o.a, o.b,) # Print the attribute

o = Manager()
print(o.a, o.b, o.c) # Print the attribute
