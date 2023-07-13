# Program to roll a dice

import random

dice_draw = {
    1: (
        " ___________",
        "|           |",
        "|           |",
        "|     °     |",
        "|           |",
        "|___________|",
    ),

    2: (
        " ___________",
        "|           |",
        "|           |",
        "|   °   °   |",
        "|           |",
        "|___________|"
    ),

    3: (
        " ___________",
        "|           |",
        "|     °     |",
        "|           |",
        "|   °   °   |",
        "|___________|"
    ),

    4: (
        " ___________",
        "|           |",
        "|   °   °   |",
        "|           |",
        "|   °   °   |",
        "|___________|"
    ),

    5: (
        " ___________",
        "|           |",
        "|   °   °   |",
        "|     °     |",
        "|   °   °   |",
        "|___________|"
    ),

    6: (
        " ___________",
        "|           |",
        "|   °   °   |",
        "|   °   °   |",
        "|   °   °   |",
        "|___________|"
    )
}

def dice_roll():
    a = random.randint(1,6)
    b = random.randint(1,6)
    print('Dice rolled:')
    print("\n".join(dice_draw[a]))
    print("\n".join(dice_draw[b]))
    print("")

while True:
    ans = input('Roll the dice? (Y/N):')
    if ans.lower() == 'y':
        dice_roll()
    elif ans.lower() == 'n':
        quit()
    else:
        print('Invalid Response')
        print("")