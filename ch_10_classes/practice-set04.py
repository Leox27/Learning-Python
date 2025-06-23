

class Calculator:

    def __init__(self, n):
        self.n = n
    
    def square(self):
        print(f"The square is {self.n*self.n}")
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")
    def square_root(self):
        print(f"The square root is {(self.n)**(1/2)}")
    
    @staticmethod # for not using self
    def greet():
        print("Hello there!")

a = Calculator(7)
a.greet()
a.square()
a.cube()
a.square_root()