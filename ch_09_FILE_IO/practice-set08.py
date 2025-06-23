# copy file of original (both are original

with open("this.txt") as f:
    content = f.read()

with open("thi_copy.txt", "w") as f:
    f.write(content)


# print(content)