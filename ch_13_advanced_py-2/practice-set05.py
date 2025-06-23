from functools import reduce

l = [1, 4, 56, 67, 67865, 67, 54]

def greater(a, b):
    if(a>b):
        return a
    return b

print(reduce(greater, l)) 