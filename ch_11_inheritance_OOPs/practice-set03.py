
class Employee:

    salary = 234
    increment =20
    
    @property # Used to get return values
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary) -1)*100

 
e = Employee()
e.salaryAfterIncrement = 280.8
print(e.increment)

