class Employee:
    a = 10
    @classmethod # Used to print the class attribute even the instance is given
    def show(cls):
        print(f"The class attribute is {cls.a}")

e = Employee()
e.a = 27

e.show()