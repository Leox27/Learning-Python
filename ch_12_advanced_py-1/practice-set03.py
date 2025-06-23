

n = int(input("Enter the number: "))

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

table = []

#  1st method
for item in list:
    table.append(item*n)

print(table)

# 2nd method

table = [n*item for item in list]
print(table)