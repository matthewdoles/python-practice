

# exercise 11 - find the sum of the first n natural numbers when given n
#               ex: 3: 3 + 2 + 1 = 6
def sum():
    n = eval(input("What is the value of n? "))
    sum = 1
    for i in range(2, n + 1):
        sum = sum + i

    print("The sum of the first", n, "natural numbers is", sum)


# exercise 12 - find the sum of the cubes the first n natural numbers when given n
#               ex: 3: 3^3 + 2^3 + 1^3 = 36
def cubed():
    n = eval(input("What is the value of n? "))
    sum = 1
    for i in range(2, n + 1):
        sum = sum + (i ** 3)

    print("The sum of the cubes for the first", n, "natural numbers is", sum)


sum()
cubed()
