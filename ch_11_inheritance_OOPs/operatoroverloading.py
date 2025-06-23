class Number:

    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"{self.value}"
    

    def __add__(self, other):
        return Number(self.value + other.value)

    def __sub__(self, other):
        return Number(self.value - other.value)

    def __mul__(self, other):
        return Number(self.value * other.value)

    def __truediv__(self, other):
        return Number(self.value / other.value)

    def __floordiv__(self, other):
        return Number(self.value // other.value)

    def __mod__(self, other):
        return Number(self.value % other.value)

    def __pow__(self, other):
        return Number(self.value ** other.value)

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value


# Test
a = Number(10)
b = Number(3)

print("Add:", a + b)
print("Sub:", a - b)
print("Mul:", a * b)
print("Div:", a / b)
print("Floor Div:", a // b)
print("Mod:", a % b)
print("Power:", a ** b)
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Less than:", a < b)
print("Less than or equal:", a <= b)
print("Greater than:", a > b)
print("Greater than or equal:", a >= b)
