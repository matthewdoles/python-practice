import math


# exercise 5 - determine if a user inputted integer is a prime number
def prime(x):
    i = 2
    while i <= math.sqrt(x):
        z = x % i
        if z == 0:
            return z
        i = i + 1
    return 1


def main():
    n = eval(input("Enter a number >> "))
    p = prime(n)

    if p != 0:
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")


# exercise 6 - modify the above program to print out every number in between 2 and n
def findprimes(x, pl):
    i = 2
    while i <= x:
        p = prime(i)
        if p != 0:
            pl.append(i)
        i = i + 1


def main2():
    n = eval(input("Enter a number >> "))
    primelist = []
    findprimes(n, primelist)
    print(primelist)


main()
# Enter a number >> 7
# 7 is a prime number

# Enter a number >> 21
# 21 is not a prime number

# Enter a number >> 71
# 71 is a prime number

main2()
# Enter a number >> 7
# [2, 3, 5, 7]

# Enter a number >> 21
# [2, 3, 5, 7, 11, 13, 17, 19]

# Enter a number >> 71
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
