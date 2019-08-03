# exercise 8 - The Gregorian epact is the number of days between Jan 1st and the previous new moon.
#              Used to find the day of Easter for a given year


def gregorianepact():
    year = eval(input("Input the 4 digit year"))
    c = year // 100
    epact = (8 + (c // 4) - c + ((8 * c + 13) // 25) + 11 * (year % 19)) % 30
    print("the Gregorian epact value is", epact)


gregorianepact()
