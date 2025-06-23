from functools import reduce # For reduce method


# Map Example
l = [1, 2, 3, 4,5, 6, 7,8 ,9 ]

square =lambda x:x*x
sqlist = map(square, l) # syntax

# print(sqlist)   # output: <map object at 0x000004BBEA0B89D0>

print(list(sqlist)) # We need to use "list()"

#####################################################################

# Filter Example

def even(n):

    if(n%2 == 0):
        return True
    return False

onlyEven = filter(even, l) #syntax

# print(onlyEven) # output: <filter object at 0x000003877C0BB6D0>
print(list(onlyEven))

###################################################################

# Reduce function

def sum(a, b):
    return a+b

print(reduce(sum, l)) # sum syntax

mul = lambda x,y:x*y

print(reduce(mul, l)) # multiplication syntax

div = lambda x,y:x/y

print(reduce(div, l)) # divison syntax
