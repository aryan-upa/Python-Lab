# These are the notes of module in Python Syllabus.

print('Ignore this line')

"""
-> Modules in Python <-
    Q: What are Module?
    A: Modules are just a python file, having just functions in it.
"""

"Random Module"

# We need to import the module first. For importing we use import keyword.

import random  # This line imports the random module.

# > Choice()
lst = [1,2,3,4,5,6,7,9,8,0,12,32,45,98,78,35,654,654,654,321,654,546,54,321,65,6]
v = random.choice(lst)
# This randomly gives a single value from a sequential data.
print(v)  # Printing the Random Choice.

# > randrange(a,b)
# Returns a data between a given range.

nm = random.randrange(1,100)  # 1 Included and 100 Excluded and between 1 to 99.
print(nm)

# > randint(a,b)
# Returns the data in the inclusive range of a and b.
# randint is faster than randrange as there is no column of step size, step size is fixed 1.

v = random.randint(1,10)  # Anything between 1 and 10 inclusive.
print(v)

# > Choice(): return multiple choices
lst = ['A','B','C','D','E']
ch = random.choices(lst,k=3)  # Here k denotes the number of choices we need.
# Choices works as it'll run random.choice on the list k number of times and all the result will be stored
# in a list and will be returned. The return type of choices method is List. We can even have the same
print(ch)  # ['A', 'E', 'D'] -> Sample Output

"""
# In random.choices() we can also apply weights making the possibilities of having some element
# more preferable than the others. The number of weights must be equal to the number of elements given
# in the original list, otherwise it raises ValueError
# For that we use the weights keyword
"""

lst = ['A','B','C','D','E']
ch = random.choices(lst,weights=(1,2,3,2,1),k=3)  # This will give 3 results but the possibilities will be
# tampered with the weights given
print(ch)  # ['D', 'C', 'C'] <- Sample Output

# > sample()
"""
The main difference between choices and sample is that sample gives only unique elements
there in sample the number of elements required in a must be less than or equal to the number
elements in the list.
If given required elements more than elements in the list will generate error, ValueError. 
"""
l = random.sample(lst,3)
print(l)  # ['C', 'D', 'A'] <- Sample Output


# > Shuffle(): use to shuffle the list.
random.shuffle(lst)
"""
Now Shuffle function does not return anything, it just changes the list given.
"""
print(lst)  # ['B', 'D', 'C', 'A', 'E'] <- Sample Output

# > random(): Very important function, It return a true value between 0 and 1 exclusive.
k = random.random()
print(k)

"OTP Generation Code"
import random
st = list(str(random.random())[2:])
"""
here we get a number from random.random().
then we convert that number to a string.
then slice the string from 2 to all, means leaving the two character of the start which are 0 and '.' .
then with the sliced string we turn it into a list.
"""
ls = random.choices(st,k=4)
# Get 4 choices from the list. The ls is also a list.
print(*ls,sep='')
# Printing the ls elements with separation '' .

'Just the above code, but in one line.'
print(*random.choices(list(str(random.random())[2:]),k=4),sep='')

# > seed()
import random
random.seed(10)  # Seeding once predicts the solution, it fixes what output random will generate.
rg = random.randrange(1,10)
print(rg)

"""
For seeding we do not run the seeding multiple times, we run seed single time, [seeding is like a fixed a sequence, 
so random will always generate same sequence] and then we know what will be the output.
"""

"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

" Math Module "
" For that we first need to import the math module. "
"""
    When we import math, it becomes an identifier and then the function, variables in it becomes it's attributes.
    We can also define the module with any other name, for this we use the as keyword.
    -> import math as m
        Now the m will work the same as math.
    we can also import definite function called customized loading of the function, for that we use the from keyword
    -> from math import pi, fact, sqrt
        this will import the attributes pi fact and sqrt and we can use that function or variable directly without using
        the '.' .
        
        then if we want to use the fact method, we can simply write.
            fact(num) instead math.fact(num)
    
    from math import * -> this will import all the methods by name, takes up much space.
    
    usually all methods return the value in float values.
"""

# from math import *
# import math
# all three methods of importing.

import math as m
"Functions in Math"
"   1. Ceil : Returns a greatest integer number greater than or equal to number given."
p = 35.12
print(m.ceil(p)) # 36

"   2. copysign(y,x) : copies the symbol of x in y."
x = -1
y = 5
print(m.copysign(y,x)) # -5.0


"   3. floor : returns the greatest integer number smaller than or equal to the number given."

p = 35.15
print(m.floor(p)) # 35


"""
Round function is a built-in function of python not a function of math.
It round offs the value given to it.
in decimal values if last significant digit is <5
    then it lowers the value
in decimal values if last significant digit is >5
    then it raises the value
if it is =5
    if digit before 5 is even
        then it lowers the value
    if digit before 5 is odd
        then it raises the value

syntax:
    Round( num , *no. of digits after '.' = 0, no digits after '.' )
"""
# Examples:
round(2.15552) # 2
round(2.35, 1) # 2.4
round(2.25, 1) # 2.2


"   4. log(x,y) : performs the log function on as log x base y. "

v = m.log(10,2)
print(v) # 3.3219280948873626

# Important application of log
# If variable is k.
k = int(input('Enter the number: '))
bt = int(m.log(k,256))+1
print(bt)


"   5. fmod(x,y) : returns the remainder when x is divided by y. "

v = m.fmod(10,3)
print(v) # 1.0











