class Employee:
    a = 10

    @classmethod # Used to print the class attribute even the instance is given
    def show(cls):
        print(f"The class attribute is {cls.a}")

    @property  # Decorator
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter # Decorator
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 27
 
e.name = "Mayur Jadhav"
print(e.fname, e.lname)

e.show()

# used for hide values behind the user known as "Abstraction"
# "Incapsulation" means we added all components in perticular class