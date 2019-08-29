from random import randrange


# exercise 8 - blackjack simulation, consult book for full problem details
def main():
    print_intro()
    n = eval(input("How many hands should I simulate? >> "))
    busts = sim_hands(n)
    print_summary(busts, n)


def print_intro():
    print("This program is designed to simulate (n) games of blackjack")
    print('and will return the probability of the dealer "busting" or')
    print("going beyond 21.")
    print()


def sim_hands(n):
    busts = 0
    for i in range(n):
        if not sim_one_hand():
            busts = busts + 1
    return busts


def sim_one_hand():
    x = sim_one_card()
    y = sim_one_card()
    hand = x + y

    while hand < 17:
        if has_ace(x) is True:
            if hand <= 10:
                x = 11
                hand = hand + 10
            else:
                x = 1

        if has_ace(y) is True:
            if hand <= 10:
                y = 11
                hand = hand + 10
            else:
                y = 1
        z = sim_one_card()
        hand = hand + z

    if hand > 21:
        return False
    else:
        return True


def sim_one_card():
    x = randrange(1, 13)
    if x == 11 or x == 12 or x == 13:
        x = 10
        return x
    else:
        return x


def has_ace(x):
    if x == 1:
        return True
    else:
        return False


def print_summary(busts, n):
    print()
    print("The dealer has a {0:0.1%} chance of busting.".format(busts/n))


if __name__ == '__main__': main()
