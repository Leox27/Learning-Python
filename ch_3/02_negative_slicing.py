name = "Mayur"

name1 = name[0:4]
print(name1)

name2 = name[:3] # It means name2 = name[0:4], Nothing means before ':' is 0
print(name2)

name3 = name[1:] # It means name3 = name[1:5], Nothing means after ':' is maximum length of string
print(name3)

name4 = name[-4:-1] # By swaping the numbers and giving +ve sign can give same output
print(name4)

name5 = name[1:4]
print(name5)

# In critical problem

name6 = name[-5:-1] # 5 is maximum length of the string
print(name6)

name7 = name[0:4] # -1 is minimum number in every string so conver -1 to 0 and 5 is maximum number so it will be 'maximum number-1 = 5-1 = 4.
print(name7)