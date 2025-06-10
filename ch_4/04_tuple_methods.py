turtle = ("Mango", 27, False, "No GF", "Rogue", "Mango")
turtle_1 = (4, 5, 6, 3)
turtle_2 = (0, 7, 8, 5, 1)

print(turtle)

count = turtle.count("Mango") # count: No. of times repeated
print(count)

i = turtle.index(False) # Find index
print(i)

total = turtle_1 + turtle_2 # Add two tuples (We can add multiple)
print(total)

print(len(turtle)) # length of tuple

mul = turtle_1*3 # Multplication i.e, no. of repetation in same tuple
print(mul)

print("Mango" in turtle) #boolean
print(10 in turtle)