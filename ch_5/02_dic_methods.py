marks = {
    "Mayur":100,
    "Sumit":98,
    "Soham":87,
    "Sanjivani":99
}

print(marks, type(marks), marks["Mayur"])

print(marks.items()) # Give pairs thhat are  saved in list
print(marks.keys()) # The single paur which connested to the seccond

marks.update({"Suraj":101, "Renuka":98, "Mayur":96}) # updation
print(marks)

print(marks.get("Somit")) #None
# print(marks("Somit")) # Return an Error

marks.pop("Mayur") # only key pop method
print(marks) # item pop

marks.popitem() # it remve the last key of the dictonary
print(marks)

