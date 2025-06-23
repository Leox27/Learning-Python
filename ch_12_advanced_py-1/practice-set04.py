# a = int(input("Enter the number: "))
# b = int(input("Enter the number: "))


# if(b == 0):
#     raise ZeroDivisionError("∞")
# else:
#     print(f"I always Right {a/b}")

# 
try:
   a = int(input("Enter the number: "))
   b = int(input("Enter the number: "))

   print(a/b)

except ZeroDivisionError as z:
    print("∞")


