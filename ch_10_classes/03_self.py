# self method in class in function

class Employee:

    language = "Python" # This is the class attribute
    salary = 100000000
    def getInfo(self):
        print(f"The language is {self.language}. the salary is {self.salary}")
    
    @staticmethod # now this fun doesn't need any object
    def greet():
        print("Good morning")

# assigning
mayur = Employee()             # Once defined as Employee in class we can use as fun
mayur.language = "Java-Script" # This is object("instance") attribute 


mayur.greet()

# We can use both alternately
# mayur.getInfo()
Employee.getInfo(mayur)
    