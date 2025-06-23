class Employee:
    a = 1

class Programmer(Employee):
        b =2

class Manager(Programmer):
            c = 3

o = Employee()
print(o.a) # print the attribute
# print(o.a, o.b) # It shows error because it doesn't have b attribute

o = Programmer()
print(o.a, o.b,) # Print the attribute
# print(o.a, o.b, o.c) # It shows error because it does'nt have c attribute 

o = Manager()
print(o.a, o.b, o.c) # Print athe attribute
