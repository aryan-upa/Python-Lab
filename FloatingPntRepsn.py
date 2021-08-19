from math import floor,fabs

def float_bin(Num: float):
    """ Binary representation of floating number. """
    a = floor(Num)
    b = Num - floor(Num)
    rem_bin = []
    for q in range(6):
        b*=2
        rem_bin.append(str(floor(b)))
        b-=floor(b)
    c = str(bin(a))[2:] + str.join("",rem_bin)
    d = len(bin(a))-3
    ret = (c, d)
    return ret

print("Enter Representation Type..."
      "\n1 -> 32 bit"
      "\n2 -> 64 bit")
ch = int(input("Enter Choice : "))
if ch==1:
    print("IEEE 32 bit Standard Chosen...")
    num = eval(input('Enter number : '))
    S = '1' if num<0 else '0'
    c_bin,e = float_bin(fabs(num))
    E = e+127
    if E>255:
        print('Unable to calculate Exponent in 32 bit form, Choose 64 bit representation. ')
        exit()
    else:
        E = str(bin(E))[2:]
    M = c_bin[1:24] + '0'*(23-len(c_bin))
    print('Resulting Binary in 32 bit representation is : ')
    print(S+E+M)
elif ch==2:
    print("IEEE 64 bit Standard Chosen...")
    num = eval(input('Enter number : '))
    S = '1' if num < 0 else '0'
    c_bin, e = float_bin(fabs(num))
    E = e + 1023
    if E > 2047:
        print('Unable to calculate Exponent.')
        exit()
    else:
        E = str(bin(E))[2:]
    M = c_bin[1:53] + '0' * (52 - len(c_bin))
    print('Resulting Binary in 64 bit representation is : ')
    print(S + E + M)
else:
    print("Wrong Input!")
