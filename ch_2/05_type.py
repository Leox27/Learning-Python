a = 10.27
t = type(a)
print(t) # class type is float

a = 1027
t = type(a)
print(t) # class type is integer

a = "10.27"
t = type(a)
print(t) # class type is string

a = 1027
t = float(a) # its valid because it gives output in float : 1027.0
t =type(t)
print(t)

# Conversion of datatype one to another
a = 10.27
t = int(a) #float to int
print(t)

a = "10.27"
print(type(a)) # to find class type : str
t = float(a) # to conver it to float :10.27
print(t)
a_int = int(t) # then convert it to int : 10
print(a_int)


