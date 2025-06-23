try:
    a = int(input("Enter a numbber: "))
    print(a)

except Exception as e:
    print(e)


else:
    print("I am in the else")

# The "try" run successfully else prints
# used in function


####### Demo code here :

# def main():
#     try:
#        a = int(input("Enter a numbber: "))
#        print(a)

#     except Exception as e:
#        print(e)

#     finally:
#         print("I am still executing")

# main()