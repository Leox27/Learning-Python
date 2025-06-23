# Constructor method *line 8*

class Employee:

    language = "Java" # This is the class attribute
    salary = 100000000

    def __init__(self, name, salary, language): # Dunder methods  called automatically (*per object)
        self.name = name
        self.salary = salary
        self.language = language

        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. the salary is {self.salary}")
    
    @staticmethod # now this fun doesn't need any object
    def greet():
        print("Good morning")

# assigning
mayur = Employee("Mayur", 70000000, "Python")  # Once defined as Employee in class we can use as fun
# mayur.name = "Mayur"
print(mayur.name, mayur.salary, mayur.language)

# rohan = Employee() 

    