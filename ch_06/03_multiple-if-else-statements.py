# if-elif-else laber

age = int(input("Enter your age: "))

# if statement no. 1
if(age % 2 == 0):
    print("Age is even...")
# End of if statement no.1

# if statement no. 2
if (age >= 18):
    print("you are eligible for concent")

elif(age < 0):
    print("You are an Idiot. your typing age in -ve")

elif(age == 0):
    print("I think you are born just")
    
else:
    print("You are not eligible for concent")
# End of i statement no.2

print("End of the program")