import random

DICE_SIDES= 6
def main():
    dice1:int=random.randint(1,DICE_SIDES)
    dice2:int=random.randint(1,DICE_SIDES)
    total:int = dice1+dice2
    print(f"Dice 1 is {dice1} Dice 2 is {dice2} total is {total}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()