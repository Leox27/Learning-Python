list = [3, 45, 6, 767, 67, 56]

# index = 0
# for item in list:
#     index += 1
#     print(f"The item number in index is {index} is {item}")

# This can be simplified using "enumerate function" better:

for index, item in enumerate(list):
    print(f"The item number in index is {index} is {item}")
