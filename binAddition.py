b1 = list(map(int,input('Enter 1st binary : ')))
print('binary 1 : ',b1)
b2 = list(map(int,input('Enter 2nd binary (of same size): ')))
print('binary 2 : ',b2)
c = [0 for q in range(len(b1)+1)]

carry = 0
i = len(b1)-1
while i>=0:
    s = b1[i] + b2[i] + carry
    c[i+1] = s % 2
    carry = int(s/2)
    i-=1
else:
    if carry:
        c[0] = 1
print('Resulting Binary is : ',*c,sep='')
