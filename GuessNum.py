import random

a = random.randrange(1,101)
# print(a)
loop = [1]
for i in loop:
    inp = int(input("Guess: "))
    if a==inp:
        print("Well Guessed!")
        print('Score',len(loop))
        exit()
    else:
        if inp>a:
            print('Greater..')
        else:
            print('Smaller..')
        # print("Wrong Guess, Try again!")
        loop.append(1)
