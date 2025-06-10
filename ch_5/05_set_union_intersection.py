s1 = {4, 65, 45, 45, 76, 78, 5, "mayur", "Suraj"}
s2 = {45, 67, 78, 8, 9, 56, "mayur"}

print(s1.union(s2)) # Union set concept: It combines the both sets but nit repeated numbers or values

print(s1.intersection(s2)) # Common values

print(s1-s2)
print(s2-s1)

print({5, 4, 65, 76}.issubset(s1))
print({45}.issuperset(s1))

print(s1.discard(65))