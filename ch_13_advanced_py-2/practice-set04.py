l = [3244,4535, 5645, 34, 45 ,3]

def divisibleByFive(n):
    if(n%5 == 0):
        return True
    return False

f = filter(divisibleByFive, l)

print(list(f))
