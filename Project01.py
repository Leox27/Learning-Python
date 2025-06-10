import random

'''
Snake = 1
Water = -1
Gun = 0

'''

computer = random.choice([-1, 1, 0])
youstr = input("Enter your choice: ")

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
 
you = youDict[youstr]

print(f"you choose: {reverseDict[you]}\nComputer choose: {reverseDict[computer]}")

if(computer == you):
    print("Match Draw")
else:
    if(computer == -1 and you == 0): # -1
        print("You Lose")

    elif(computer == -1 and you == 1): # -2
        print("You Win")

    elif(computer == 1 and you == 0): # 1
        print("You Win")

    elif(computer == 1 and you == -1): # 2
        print("You Lose")

    elif(computer == 0 and you == 1): # -1
        print("You Lose")

    elif(computer == 0 and you == -1): # 1
        print("You Win")

    else:
        print("Something went wrong.")



# Another one method based on this large code is we can write by simplifying both values that i comment out in every line in end og the loop reducing this given code that is code given below

# if((computer - you) == -1 or (computer - you) == 2):
#     print("You lose")

# else:
#     print("You Win")

