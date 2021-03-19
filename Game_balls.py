'''
---The Ball Game---
The only to make to sure that computer wins everytime is to make the net ball picked up in a turn comprising men and
computer results in 5, in that manner only, we'll be left with 1 single ball at the 21st turn, which will be of human,
and at that moment he'll be left with 1 ball only, resulting in computer's win in the game.
'''

tot= 51
print("---The Ball Game---")
input("Press any key to continue...")
print("\nRules:\n"
      "1. Player must pick only less than 5 and more than 0 ball(s) at a time.\n"
      "2. Last ball picker will lose.\n"
      "3. Entering Invalid input will result in end of game in losing state.\n")
input("Press any key to continue...")
print("Total balls at the start of the game are 51.")
for i in range(1,52):
    if tot>1:
        if i%2!=0:
            inp = int(input("Your Turn: "))
            if inp>=5 or inp==0:
                print("Invalid Input: ")
                print("And, you lost the game, you Human.")
                exit()
            else:
                tot-=inp
                print(f'Remaining balls are {tot}.')
        else:
            print("Computer's turn: ")
            comp= 5-inp
            print(f"Computer: I pick {comp}.")
            tot = tot - comp
            print(f"Remaining balls are: {tot}")
    else:
        print("Now as only 1 ball is remaining and its your turn.")
        print("So, pick it.\nPICK ITT....")
        print("\nThere you go."
              "\n\nYou Loser."
              f"\nComputer: 😈😈 (Evil Laugh)")
        break

print("\nGame Finished!")