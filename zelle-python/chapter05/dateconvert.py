def dateformat():
    date = input("Enter a date (mm/dd/yyy): ")

    month, day, year = date.split("/")

    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    month = months[int(month) - 1]
    print("The converted date is: ", month, day+",", year)


def dateformat2():
    day, month, year = eval(input("Enter a day, month, and year numbers: "))
    date1 = str(month) + "/" + str(day) + "/" + str(year)
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    month_str = months[month - 1]
    date2 = month_str + " " + str(day) + ", " + str(year)
    print("The converted date is", date1, "or", date2)


# exercise 1 - date convert formatting
def dateformat3():
    date = input("Enter a date (mm/dd/yyy): ")

    month, day, year = date.split("/")

    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    month_str = months[int(month) - 1]
    print("The converted date is {0}/{1}/{2} or {3} {1}, {2}".format(month, day, year, month_str))
    # Enter a date (mm/dd/yyy): 05/18/1995
    # The converted date is 05/18/1995 or May 18, 1995


dateformat()
dateformat2()
dateformat3()
