'''
***
* *
***
'''

n = int(input("Enter the number: ")) # "n" is the No. of layers want to print 

for i in range(1, n+1):
  
    if(i == 1 or i == n):            # i is no. of layers to be printing
      print("*"* n, end="")

    else:
      print("*", end="")       
      print(" "* (n-2), end="")
      print("*", end="")

    print("\n") # For next line
