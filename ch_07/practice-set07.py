'''
  *_
 ***
*****
'''

n = int(input("Enter the number: ")) # "n" is the No. of layers want to print 

for i in range(1, n+1):

   print(" "* (n-i), end="")
   print("*"* (2*i-1), end="")
   print("\n")