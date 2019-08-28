import math


# exercise 5 - goldbach conjecture, every even number is the sum of two prime numbers
def prime(x):
    i = 2
    while i <= math.sqrt(x):
        z = x % i
        if z == 0:
            return z
        i = i + 1
    return 1


def findsum(x, pl):
    p1 = 2
    p2 = 2
    total = 0
    while total != x:
        i = prime(p1)
        if i == 0:
            p1 = p1 + 1
        else:
            total = 0
            p2 = 2
            while total < x:
                j = prime(p2)
                if j == 0:
                    p2 = p2 + 1
                else:
                    total = p1 + p2
                    if total < x:
                        p2 = p2 + 1
        if total != x:
            p1 = p1 + 1

    pl.append(p1)
    pl.append(p2)


def main():
    n = eval(input("Enter an even number >> "))
    if n % 2 != 0:
        print("Sorry, that was not an even number.")
        main()
    else:
        primesum = []
        findsum(n, primesum)
        print("The two primes that add together to get", n, "are", primesum)


main()
# Enter an even number >> 10
# The two primes that add together to get 10 are [3, 7]

# Enter an even number >> 56
# The two primes that add together to get 56 are [3, 53]

# Enter an even number >> 100
# The two primes that add together to get 100 are [3, 97]
