import random

NUM_SIDES = 6

def roll_dice():

    die1 = random.randint(1,NUM_SIDES)
    die2 = random.randint(1,NUM_SIDES)

    total = die1+die2
    print(f"Die1 :{die1} , Die2 : {die2} , Total : {total}")

def main():

    die1:int = 10

    print(f"die1 is :{die1}")

    for _ in range(3):
        roll_dice()
        print(f"Die1 in main remain same {die1}")
       
if __name__ == "__main__":
 
   main()