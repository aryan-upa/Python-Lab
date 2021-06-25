# The characters which are in string 1 but not in string 2.
st1 = set(input('Enter 1st String: '))
st2 = set(input('Enter 2nd String: '))

s = st1 - st1.intersection(st2)
print('The no. of characters are : ',len(s),'\nAnd he characters are : ',*s)
