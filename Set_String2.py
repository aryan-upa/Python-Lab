# WAP to find out words which are either in string 1 or in string 2 but not in both.

st1 = set(input('Enter string 1 : '))
st2 = set(input('Enter string 2 : '))

s = st1.symmetric_difference(st2)
print('The characters which are either in string 1 or in string 2 are :',len(s))
print(f'The characters are : {s}')
