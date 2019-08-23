

# exercise 7 - alter Fibonacci program from Chapter 3 to use functions
def calculate(n, x, y):
    sequence = []
    for i in range(n):
        z = x + y
        sequence.append(z)
        y = x
        x = z
        print(sequence)
    return z


def fibonacci():
    n = eval(input("What number in the Fibonacci sequence would you like to see?: "))
    x = 1
    y = 0
    z = calculate(n, x, y)
    print("Position", n, "equals", z, "in the Fibonacci sequence")


fibonacci()
# What number in the Fibonacci sequence would you like to see?: 6
# [1]
# [1, 2]
# [1, 2, 3]
# [1, 2, 3, 5]
# [1, 2, 3, 5, 8]
# [1, 2, 3, 5, 8, 13]
# Position 6 equals 13 in the Fibonacci sequence
