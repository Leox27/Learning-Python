try:
    a = int(input("Enter a numbber: "))
    print(a)

except Exception as e:
    print(e)
except TypeError as a:
    print(a)
except ValueError as v:
    print(v)

print("Thank You")
