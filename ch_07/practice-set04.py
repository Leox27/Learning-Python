# Prime number print

n = int(input("Enter the numeber: "))

for i in range(2, n):                # not from 1
    if(n%i) == 0:
        print("Number is not Prime.")
    else:
        print("It's Prime.")
        break                        # No need to go n no. of numbers