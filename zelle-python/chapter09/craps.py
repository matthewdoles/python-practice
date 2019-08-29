from random import randrange

def main():
    print("Would you like to play a game of craps?")
    x = input("Press <Enter> to roll dice >> ")
    dice1 = randrange(1, 6)
    dice2 = randrange(1, 6)
    roll = 1
    initial_total = dice1 + dice2
    print("Roll", roll, " - ", "Die 1 =", dice1, "  Die 2 =", dice2, "  and Total =", initial_total)
    if initial_total == 7 or initial_total == 11:
        print("Congrats! You have won with an initial roll of", initial_total)
    elif initial_total == 2 or initial_total == 3 or initial_total == 12:
        print("Sorry! You have lost with an initial roll of", initial_total)
    else:
        print("Looks like you will be re-rolling to try and get a", initial_total)
        roll_total = 0
        while not rerolling_over(initial_total, roll_total):
            x = input("\nPress <Enter> to roll dice >> ")
            dice1 = randrange(1, 6)
            dice2 = randrange(1, 6)
            roll_total = dice1 + dice2
            roll = roll + 1
            print("Roll", roll, "-", "Die 1 =", dice1, ", Die 2 =", dice2, ",  Total =", roll_total)

        if roll_total == initial_total:
            print("Congrats! You won by rolling a", initial_total, "again.")
        else:
            print("Sorry! You rolled a 7, better luck next time")


def rerolling_over(initial_roll, current_roll):
    return initial_roll == current_roll or current_roll == 7

main()