s1 = {q**2 for q in range(1,11)} # Set holding Squares of value ranging from 1 to 10
s2 = {q**3 for q in range(1,11)} # Set holding Cubes of value ranging from 1 to 10

print('Initial Elements of Set:\n')
print(s1)
print(s2)

print('Demonstrating pop method...')
r = int(input('Enter how many pops (less than length): '))
for i in range(r):
    print(f'Elements popped from s1 and s2 on {i+1} turn')
    print(s1.pop())
    print(s2.pop())

print('Elements of Set now: ')
print(s1)
print(s2)

print('Demonstrating Update method...')
ls = list(map(int,input('Enter elements to add: ').split()))
c = int(input('Which Set (1/2) : '))
if c==1:
    s1.update(ls)
else:
    s2.update(ls)

print('Elements of Set now: ')
print(s1)
print(s2)

print('Demonstrating remove method')
print('Please make sure that element is "in" that set which you'
      ' want to remove otherwise it\'ll generate an error.')
s = int(input('Enter element to remove: '))
c = int(input('Which Set (1/2) : '))
if c==1:
    s1.remove(s)
else:
    s2.remove(s)

print('Elements of Set now: ')
print(s1)
print(s2)

print('Demonstrating add method')
s = int(input('Enter element to add: '))
c = int(input('Which Set (1/2) : '))
if c==1:
    s1.add(s)
else:
    s2.add(s)

print('Elements of Set now: ')
print(s1)
print(s2)

print('Demonstrating clear method')
s1.clear()
s2.clear()
print('Elements of Set now: ')
print(s1)
print(s2)
