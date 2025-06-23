a = "{} and {} are best friends".format("Mayur", "Suraj")
print(a)

# insert index for args

# We can insert index also
a = "{0} and {1} are best friends".format("Mayur", "Suraj")
print(a)

# We can change the index also
a = "{1} and {0} are best friends".format("Mayur", "Suraj")
print(a)

# Eve we can assign same index
a = "{1} and {1} are best friends".format("Mayur", "Suraj")
print(a)