s1 = set(input('Enter elements of set 1: ').split())
s2 = set(input('Enter elements of set 2: ').split())

# Union Operation
print('Union Operation: ')
print(s1.union(s2))

# Intersection Operation
print('Intersection Operation: ')
print(s1.intersection(s2))

# Difference Operation
print('Difference Operation: ')
print(s1.difference(s2))

# Symmetric Difference Operation
print('Symmetric Difference Operation: ')
print(s1.symmetric_difference(s2))
