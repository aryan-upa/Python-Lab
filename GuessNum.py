import random

a = random.randrange(10)
# print(a)
loop = [1]
for i in loop:
    inp = int(input("Enter the Input: "))
    if a==inp:
        print("Well Guessed!")
        exit()
    else:
        print("Wrong Guess, Try again!")
        loop.append(1)
