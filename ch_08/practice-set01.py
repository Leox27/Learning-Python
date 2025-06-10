def greatest(a, b, c):
    if(a>b or a>c):
        return a
    elif(b>a or b>c):
        return b
    else:
        return c
    
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))

print(greatest(a, c, b)) # it will print correct value even i place parameters back and forth
    
