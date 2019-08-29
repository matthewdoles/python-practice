from random import random


# exercise 3 - simulate the game of volleyball, sames rules but winner must win by 2
def main():
    print_intro()
    prob1, prob2, n = get_inputs()
    wins1, wins2 = sim_games(n, prob1, prob2)
    print_summary(wins1, wins2)


def print_intro():
    print("This program simulates a game of volleyball between two")
    print("teams called '1' and '2'. The abilities of each team is ")
    print("indicated by a probability (a number between 0 and 1) that")
    print("the team wins the point when serving. Team 1 always")
    print("has the first serve")


def get_inputs():
    a = eval(input("\nWhat is the prob. Team 1 wins a serve? "))
    b = eval(input("What is the prob. Team 2 wins a serve? "))
    n = eval(input("How many games are to be simulated? "))
    return a, b, n


def sim_games(n, prob1, prob2):
    wins1 = 0
    wins2 = 0
    for i in range(n):
        score1, score2 = sim_one_game(prob1, prob2)
        if score1 > score2:
            wins1 = wins1 + 1
        else:
            wins2 = wins2 + 1
    return wins1, wins2


def sim_one_game(prob1, prob2):
    score1 = 0
    score2 = 0
    serving = "1"
    while not game_over(score1, score2):
        if serving == "1":
            if random() < prob1:
                score1 = score1 + 1
            else:
                serving = "2"
        else:
            if random() < prob2:
                score2 = score2 + 1
            else:
                serving = "1"
    return score1, score2


def game_over(a, b):
    return (a >= 15 and a >= b + 2) or (b >= 15 and b >= a + 2)


def print_summary(wins1, wins2):
    n = wins1 + wins2
    print("\nGames simulated:", n)
    print("Wins for Team 1: {0} ({1:0.1%})".format(wins1, wins1 / n))
    print("Wins for Team 2: {0} ({1:0.1%})".format(wins2, wins2 / n))


if __name__ == '__main__':
    main()
