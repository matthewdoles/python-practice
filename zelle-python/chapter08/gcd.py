

# exercise 8 - find the GCD of two user inputted numbers
def gcd(n, m):
    while m != 0:
        n, m = m, n % m

    return n


def main():
    x, y = eval(input("Enter two numbers (comma separated) >> "))
    ans = gcd(x, y)
    print("The greatest common denominator for", x, "and", y, "is", ans)


main()
# Enter two numbers (comma separated) >> 10, 25
# The greatest common denominator for 10 and 25 is 5

# Enter two numbers (comma separated) >> 21, 99
# The greatest common denominator for 21 and 99 is 3

# Enter two numbers (comma separated) >> 32, 77
# The greatest common denominator for 32 and 77 is 1
