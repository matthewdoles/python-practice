

# exercise 9 - use formula to determine what day Easter will be on (only works between 1982 - 2048)
def easter(year):
    if 1982 <= year <= 2048:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7
        if (d + e) > 9:
            print("Easter falls on April {}.".format(d + e - 9))
        else:
            print("Easter falls on March {}.".format(22 + d + e))
    else:
        print("Year is out of range")


# exercise 10 - fix the Easter formula for years where it produces a week that is too long
def easter2(year):
    if 1900 <= year <= 2099:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7
        if (d + e) > 9:
            if year == 1954 or 1981 or 2049 or 2076:
                d = d - 7
                print("Easter falls on April {}.".format(d + e - 9))
            else:
                print("Easter falls on April {}.".format(d + e - 9))
        else:
            if year == 1954 or 1981 or 2049 or 2076:
                d = d - 7
                print("Easter falls on March {}.".format(22 + d + e))
            else:
                print("Easter falls on March {}.".format(22 + d + e))
    else:
        print("Year is out of range")


def main():
    year = eval(input("Input a year: "))
    easter2(year)


main()
