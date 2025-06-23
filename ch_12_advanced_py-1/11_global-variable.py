a = 45

def fun():
    global a
    a = 27
    print(a)

fun()
print(a)

# global variable prints under the function value