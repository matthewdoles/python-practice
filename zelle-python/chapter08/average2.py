# while loop - average example
def avg2():
    sum = 0.0
    count = 0
    moredata = "yes"
    while moredata[0] == "y":
        x = eval(input("Enter a number >> "))
        sum = sum + x
        count = count + 1
        moredata = input("Dp you have more numbers (yes or no): ")

    print("\nThe average of the numbers is", sum / count)


avg2()
