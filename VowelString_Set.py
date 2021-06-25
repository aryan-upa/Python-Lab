S = set(input('Enter the elements of the set: ').split())
Ns = set()
for q in S:
    ts = set(q)
    if len(ts.intersection({'a','e','i','o','u'}))>0:
        Ns.add(q)
print('Strings containing any vowel :',Ns)
