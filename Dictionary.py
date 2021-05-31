# Just like real life Dictionary where we try to find out the meaning knowing the word.
# Similar we will do here:
#     we have a key : and we have a value
#     therefore
#         Dic = {key1:Mean1, key2:Mean2, key3:Mean3...}
# Dictionary is "Unordered"

D = {'book':'kitaab', 'apple': 'seb', 'where':'kahan'}
print(D)

# Similarly we can store other data types as well
D = {'Aryan': [50,80,90], 'Priyanshi':[88,92,100], 'Rohit': [84,52,67]}
print(D)

# We can store numbers as well
D = {'Amit':9513551663, 'Utkarsh':1234689845}
print(D)

# We need to make keys which are of Immutable data type.
# Immutable Types: [String, Tuples, Sets, Number, frozenset]
# If we give any mutable data type to place where Immutable data type was to be given we
# get an Error:'Un hashable' Datatype

D = {(0,1):'Aryan', (0,2):'Values'}
print(D)

# Dictionary can be Nested but we can use Dictionary only in Values not in Keys.
# Keys must be Unique, there must be no redundancy.
# But even if we give same key to two different Values, it'll not generate any error
# but the length of Dictionary will be only the length of Unique keys.
# In that case we have two keys of same values, the later value is admitted.

D = {'Aryan': 123, 'Amit': 456, 'Aryan': 789}
print(D, len(D))  # {'Aryan': 789, 'Amit': 456} 2 The Later value of key is admitted.

# To extract the values
# D.get(Key) = Value
# D[Key] = Value -> Here we can also use Indexing
# D[Values] = Key

D = {'Sam': 29000, 'Mi': 18000, 'Iphone': 95000, 'Nokia': 30000, 'Hua': 45000}
print(D['Sam'])  # 29000
print(D.get('Mi'))  # 18000
# The difference between these two is when we ask value of a key which do not exist.
print(D['MIA'])  # KeyError
print(D.get('MIA'))  # None
