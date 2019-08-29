from random import random


def main():
    print_intro()
    n = eval(input("How many steps should be simulated each trip? "))
    avg_distance = simulate_walks(n)
    print("The object will travel an average of", avg_distance, "steps.")


def print_intro():
    print("This program simulates a random walk in one dimension, where the")
    print("object will move either forward or backward at random.")
    print('User provided "n" represents the number of steps per trip.')
    print("The program will simulate 1000 trips, and return ")
    print("the average distance traveled per trip.")


def simulate_walks(n):
    distance = 0
    for i in range(1000):
        steps = sim_steps(n)
        distance = distance + steps
    if distance != 0:
        distance = distance / 1000
    return distance


def sim_steps(n):
    steps = 0
    for i in range(n):
        x = 2 * random()
        if x > 1:
            steps = steps + 1
        else:
            steps = steps - 1
    return steps


if __name__ == '__main__': main()
