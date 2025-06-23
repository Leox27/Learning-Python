

file = open("file.txt", "r") # Ctrated file same path

# lines = file.readlines()

# print(lines, type(lines))

# file.close()


'''

line1 = file.readline()
print(line1, type(line1))

line2 = file.readline()
print(line2, type(line2))

line3 = file.readline()
print(line3, type(line3))

line4 = file.readline()
print(line4, type(line4))

line5 = file.readline()
print(line5, type(line5))

file.close()

'''
 

line = file.readline()
while(line != ""):
    print(line)
    line = file.readline()

file.close() 