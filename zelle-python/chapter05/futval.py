

# exercise 12 - improve on the future value calculator from chapter 1 - print into formatted table
def futval():
    print("This program calculates the future value of a 10-year investment.\n")

    principal = 900
    apr = 5

    print("{0:<7}{1:<10}".format("Year", "Value"))
    print("----------------")

    for i in range(10):
        principal = principal * (1 + .01 * apr)

        print("{0:<7}${1:<}.{2:0^2}".format(i + 1, int(principal), int(principal % 1 * 100)))


futval()

# This program calculates the future value of a 10-year investment.
#
# Year   Value
# ----------------
# 1      $945.00
# 2      $992.25
# 3      $1041.86
# 4      $1093.95
# 5      $1148.65
# 6      $1206.80
# 7      $1266.39
# 8      $1329.70
# 9      $1396.19
# 10     $1466.00