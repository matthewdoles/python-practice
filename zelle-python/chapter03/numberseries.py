

# exercise 13 - sum a series of user inputted numbers and print a total sum
def numberssum():
    n = eval(input("How many numbers do you wish to sum? "))
    sum = 0

    for i in range(n):
        print("Number", i + 1, "-", end=" ")
        sum = sum + eval(input())

    print(sum)


# exercise 14 - find the average of a series of user inputted numbers
def numbersaverage():
    n = eval(input("How many numbers do you wish to average? "))
    sum = 0

    for i in range(n):
        print("Number", i + 1, "-", end=" ")
        sum = sum + eval(input())

    print(sum / n)


numberssum()
numbersaverage()
