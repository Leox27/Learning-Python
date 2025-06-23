f = open("p1_poem.txt")
content = f.read()

if("Twinkle twinkle" in content):
    print("Twinkle twinle is present in content")
else:
    print("Not present")

f.close()



# if("I am" in content):
#     print("Twinkle twinle is present in content")
# else:
#     print("Not present")