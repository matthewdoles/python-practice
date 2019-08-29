from random import random

# exercise 1 - revise racquetball simulation so that it is a best of n games, and serves are alternated
def main():
    print_intro()
    prob1, prob2, n = get_inputs()
    wins1, wins2 = sim_games(n, prob1, prob2)
    print_summary(n, wins1, wins2)


def print_intro():
    print("This program simulates a match of racquetball between two")
    print("players called '1' and '2'. The abilities of each player is ")
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player 1 always")
    print("has the first serve in even games, and player 2 in odd games.")


def get_inputs():
    a = eval(input("\nWhat is the prob. Player 1 wins a serve? "))
    b = eval(input("What is the prob. Player 2 wins a serve? "))
    n = eval(input("How many games is the series a best of? "))
    return a, b, n


def sim_games(n, prob1, prob2):
    wins1 = 0
    wins2 = 0
    game = 1
    while not series_over(wins1, wins2, n):
        score1, score2, game = sim_one_game(prob1, prob2, game)
        if score1 > score2:
            wins1 = wins1 + 1
        else:
            wins2 = wins2 + 1
    return wins1, wins2


def sim_one_game(prob1, prob2, game):
    score1 = 0
    score2 = 0
    serving = "1"
    if game % 2 == 0:
        serving = "2"
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
    game = game + 1
    return score1, score2, game


def game_over(a, b):
    return a == 15 or b == 15


def series_over(a, b, n):
    return a > n / 2 or b > n / 2


def print_summary(n, wins1, wins2):
    games_played = wins1 + wins2
    print("\nBest of:", n)
    print("Games played:", games_played)
    print("Wins for A: {0} ({1:0.1%})".format(wins1, wins1 / games_played))
    print("Wins for B: {0} ({1:0.1%})".format(wins2, wins2 / games_played))


if __name__ == '__main__':
    main()
