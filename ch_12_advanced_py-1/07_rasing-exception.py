a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if(b == 0):
    raise ZeroDivisionError("Baap ko mat sikha")
else:
    print(f"The division of a/b is {a/b}")
