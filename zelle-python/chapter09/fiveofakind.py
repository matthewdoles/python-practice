from random import randrange


# exercise 11 - simulate the probability of rolling five of a kind given n rolls
def main():
    print_intro()
    n = eval(input("How many rolls should we simulate >> "))
    total = sim_rolls(n)
    print_summary(n, total)


def print_intro():
    print("This program simulates the rolling of five six-sided")
    print("to help predict the probability of rolling five-of-a-kind.")


def sim_rolls(n):
    total = 0
    for i in range(n):
        if five_of_a_kind():
            total = total + 1
    return total


def five_of_a_kind():
    a, b, c, d, e = sim_one_roll()
    if a == b == c == d == e:
        return True
    else:
        return False


def sim_one_roll():
    dice = []
    for i in range(5):
        x = randrange(1, 6)
        dice.append(x)
    return dice


def print_summary(n, total):
    print("\nRolls simulated: ", n)
    print("Five of a Kind: {0} ({1:0.1%})".format(total, total / n))


if __name__ == '__main__': main()
