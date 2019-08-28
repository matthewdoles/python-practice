

# exercise 4 - calculate the Syracuse sequence when given a user input
#              sequence stops when the number 1 is reached
def syracuse(x, sequence):
    if x % 2 == 0:
        x = int(x / 2)
        sequence.append(x)
    elif x % 2 == 1:
        x = int(3 * x + 1)
        sequence.append(x)
    return x


def main():
    n = eval(input("What is the starting value you would like to see for the Syracuse sequence? "))
    sequence = [int(n)]
    while n != 1:
        n = syracuse(n, sequence)

    print(sequence)


main()
