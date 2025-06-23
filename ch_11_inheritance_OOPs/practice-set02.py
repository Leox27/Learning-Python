class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    
    @staticmethod # for not using self
    def bark():
        print("BOW BOW")

object = Dog()

object.bark()