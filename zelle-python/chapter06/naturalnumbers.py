

# exercise 4 - write functions to sum first n natural number given n
#              and the sum of the cubes of the first n natural numbers
def sumN(n):
    sum = 1
    for i in range(2, n + 1):
        sum = sum + i
    return sum


def sumNCubes(n):
    sum = 1
    for i in range(2, n + 1):
        sum = sum + (i ** 3)
    return sum


def main():
    n = eval(input("What is the value of n? "))
    sum = sumN(n)
    cubed_sum = sumNCubes(n)
    print("The sum of the first", n, "natural numbers is", sum)
    print("The sum of the cubes for the first", n, "natural numbers is", cubed_sum)


main()
# What is the value of n? 3
# The sum of the first 3 natural numbers is 6
# The sum of the cubes for the first 3 natural numbers is 36
