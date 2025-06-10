marks =int(input("Enter your marks: "))

if(marks <= 100 and marks >=91):
    grade = "Ex"

elif(marks < 90 and marks >=81):
    grade="A"

elif(marks < 80 and marks >=71):
    grade = "B"

elif(marks < 70 and marks >=61):
    grade = "C"

elif(marks < 50):
    grade = "D"

print("Your grade is : ", grade)
