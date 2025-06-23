

list = [1, 2, 3, 4, 5, 6, 7]
squaredList = []


# 1st method

for item in list:
    squaredList.append(item*item)

print(squaredList)

# 2nd method

squaredList = [item*item for item in list]
print(squaredList)