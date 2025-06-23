

class Employee: # Parent class or base class

    company = "TCS"
    name = "Default name"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")

class Coder:

    language = "Python" 
    def printLanguage(self):
        print(f"Out of all languages is your Language {self.language}")

# Inheritance class which is derived from parent class or base class
class Programmer(Employee, Coder): 
    company = "TCS Nvidia"
    def showLanguage(self):
        print(f"The company is {self.company} And he is good at {self.language} language")


# a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLanguage()
