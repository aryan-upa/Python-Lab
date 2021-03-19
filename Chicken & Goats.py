'''
The Goat and Chicken Problem
Using equations we can solve this qustion.
Let p = Total no. of foots & q = Total no. of heads
and Let, x = no. of chicken and y represent no. of goats.
Then,
            2x + 4y = p
            x + y = q
Solving both gives us:
            x = (4q-p)/2
            y = q-x
Which will give us the desired values of goats and chickens.
'''

p = int(input("Enter the number of foots: "))
q = int(input("Enter the number of heads: "))

x = int((4*q - p)/2)
y = q-x
print(f"The number of goats: {y}")
print(f"The number of chickens: {x}")
