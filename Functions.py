"""

Functions in python are defined by block keyword 'def'
def function_name (Formal parameter): # Function Definition
    Syntax_in_Python

function_name(Actual Parameter) # Function Call

What we passes is Actual parameter
What function receives is Formal parameter.

In General we never use the print statement in Function.

"""


def perfect(num):
    ls = []
    for q in range(1,num):
        if num%q==0:
            ls.append(q)
    if sum(ls) == num:
        return True
    else:
        return False


inp = int(input('Enter num: '))
print('Perfect Number') if perfect(inp) else print('Not Perfect')


def prime(num):
    from math import sqrt
    if num==1:
        return False
    elif num==2:
        return True
    else:
        q = 2
        while q<=sqrt(num):
            if num % q==0:
                return False
        else:
            return True


inp = int(input('Enter num: '))
print('Prime Number') if perfect(inp) else print('Not Prime')

