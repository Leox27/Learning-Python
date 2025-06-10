friends = ["Mayur", "Suraj", "Varun", "Vishwas", "Sohel", "Abhishek", "Sudarshan"]
nums = [7, 6, 5, 3, 4, 2, 1]

print(friends)

pop = friends.pop(5)
print(friends)

append = friends.append("Abhishek")
print(friends)

friends.insert(0, "Atman") # We add String in list in index [0], bcz List are Immutable.
print(friends) # OUTPUT: ['Atman', 'Mayur', 'Suraj', 'Varun', 'Vishwas', 'Sohel', 'Sudarshan', 'Abhishek']

nums.sort()
print(nums)

nums.reverse()
print(nums)

print(nums.count(4))
print(friends.count("Mayur"))