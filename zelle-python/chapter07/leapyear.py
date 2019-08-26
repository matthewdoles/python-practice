

# exercise 11 - determine if a year is a leap year, divisible by 4 or is a century
def main():
    year = eval(input("Input a year: "))
    if (year % 4) != 0:
        print("{} is not a leap year.".format(year))
    else:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{} is a leap year.".format(year))
            else:
                print("{} is not a leap year.".format(year))
        else:
            print("{} is a leap year.".format(year))


main()
