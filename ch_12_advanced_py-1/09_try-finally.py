try:
    a = int(input("Enter a numbber: "))
    print(a)

except Exception as e:
    print(e)

finally:
    print("Hey I am in finally")

# "finally" prints their statement even the code gives error