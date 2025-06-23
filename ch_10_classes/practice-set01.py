

class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pincode): # constructor
        self.name = name
        self.salary = salary
        self.pincode = pincode

p = Programmer("Mayur", 2700000, 413002)
print(p.name, p.salary, p.pincode, p.company)

s = Programmer("Suraj", 2700000, 413002)
print(s.name, s.salary, s.pincode, s.company) 

