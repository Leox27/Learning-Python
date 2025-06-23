'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 4
sum(5) = 1 + 2 + 4 + 5

sum(n) = 1 + 2 + 3 + 4 + n
sum(n) = sum(n-1) 

''' 

def sum(n):
    if(n == 1):
        return 1
    return sum(n-1) + n

n = int(input("Enter the number: "))

# print(f"The sum is:{sum(n-1) + 1}") -> For perfection

print(sum(n))


