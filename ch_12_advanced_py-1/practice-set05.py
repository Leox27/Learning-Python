n = int(input("Enter the number: "))

table = [n*item for item in range(1, 11)]

with open("Table.txt", "a") as f:
    # f.write(str(table) + "\n")
    f.write(f"The Table of {n}: is {str(table)} \n")