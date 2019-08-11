def findabbrev():
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    n = eval(input("Enter a month number (1 - 12): "))

    pos = (n-1) * 3
    month_abbrev = months[pos:pos+3]
    print("The month abbreviation for", n, "is", month_abbrev)


def fullmonth():
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    n = eval(input("Enter a month number (1 - 12): "))
    print("The month  for", n, "is", months[n - 1])


findabbrev()
fullmonth()
