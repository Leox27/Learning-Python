set1 = {1, 2, 3}
set2 = {3, 4, 5}

# add() elemnts in set1
set1.add(6) # OUTPUT: set2 = {3, 4, 5, 6}
print(set1)

# difference() method
print(set1.difference(set2))
print(set2.difference(set1))

# intersection() method (common element in both set)
print(set1.intersection(set2))

# union() method (print every element but not repeated)
print(set1.union(set2))
print(set2.union(set1))

# issubset() method (elements that only belongs to that perticular set)
print({1, 2, 3}.issubset(set1))
print({1, 2,}.issubset(set2))

# issuperset() method ( )
print(set1.issuperset({3}))

# set.pop() method (remov3s 1st element in that set)
# print(set1.pop())
# print(set1)

# clear() method
# set1.clear()
# print(set1)