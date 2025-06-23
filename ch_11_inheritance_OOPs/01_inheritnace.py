

class Employee: # Parent class or base class
    company = "TCS"
    salary = 1200000
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

# class Programmer:
#     company = "Nvidia"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} And he is good at {self.language} language")

# Inheritance class which is derived from parent class or base class
class Programmer(Employee): 
    company = "TCS Nvidia"
    name = "Mayur"
    language = "Python"
    def showLanguage(self):
        print(f"The name is {self.name} And he is good at {self.language} language")


a = Employee()
b = Programmer()

# b.show()
# b.showLanguage()

print(a.company, b.company)
