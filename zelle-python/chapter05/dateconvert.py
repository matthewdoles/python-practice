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


dateformat()
dateformat2()
