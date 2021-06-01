def Mod1():
    def Area_Rec(x,y):
        area = x*y
        return area

    inp = input('Enter L<space>B: ')
    l,b = map(int,inp.split())
    print('Area of Rectangle: ',Area_Rec(l,b))


def Mod2():
    def Circ_fun(r):
        from math import pi
        peri = 2 * pi * r
        area = pi * r * r
        return area,peri

    inp = int(input('Enter Radius: '))
    A,P = Circ_fun(inp)
    print(f'Perimeter {P} and Area of Circle {A}')


def Mod3():
    def pow_new(base,to_the):
        power = base**to_the
        return power

    inp = input('Enter Base<space>Power: ')
    b,p = map(int,inp.split())
    print('Solution: ',pow_new(b,p))


def Mod4():
    def eligible(age):
        if age>=18:
            return True
        return False

    inp = int(input('Enter Age: '))
    A = eligible(inp)
    print('Person is Eligible.') if A else print('Person in Ineligible.')


def Mod5():
    def eve_Check(num):
        if num & 1==1:
            return False
        return True

    inp = int(input('Enter Number: '))
    A = eve_Check(inp)
    print('Even') if A else print('Odd')


print('Basic Python Functions')
recall = 1
while recall:
    print('Enter Choice:\n'
          '1. Area of rectangle\n'
          '2. Perimeter and Area of Circle\n'
          '3. Base to Power calculation\n'
          '4. Voting eligibility\n'
          '5. Even and Odd check\n')
    inp = int(input('Enter Choice (1-5): '))
    eval(f'Mod{inp}()')
    print('\nAgain?? 1-> Yes, 0-> No')
    recall = int(input('Enter 1 or 0: '))

