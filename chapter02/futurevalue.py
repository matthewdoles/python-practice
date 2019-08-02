# a program to compute the value of an investment
# carried 10 in years into the future


def futurevalue():
    print("This program calculates the future value of a 10 year investment")
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))

    for i in range(10):
        principal = principal * (1 + apr)

    print("The value in 10 years is: ", principal)


# exercise 5 - alter to take the years as an input from the user
def futurevalue2():
    print("This program calculates the future value of an investment with a given interest rate and years")
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the number of years: "))

    for i in range(years):
        principal = principal * (1 + apr)

    print("The value in", years, "year(s) is: ", principal)


# exercise 6 - alter to where the user invests a fixed amount every year
def futurevalue3():
    print("This program calculates the future value of an investment ", end="")
    print("with a given interest rate, years, and annual fixed investment")
    principal = eval(input("Enter the initial principal: "))
    annual = eval(input("Enter the annual fixed investment principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the number of years: "))

    for i in range(years):
        principal = principal + annual
        principal = principal * (1 + apr)

    print("The value in", years, "year(s) is: ", principal)


# exercise 7 - alter to where the interest rate compounds a given number of periods each year
def futurevalue4():
    principal = eval(input("Enter the initial principal: "))
    rate = eval(input("Enter the interest rate: "))
    periods = eval(input("Enter the number of compounding periods per year: "))
    years = eval(input("Enter the number of years for the investment: "))

    nominal_rate = rate / periods

    for i in range(periods * years):
        principal = principal * (1 + nominal_rate)

    print("The value in 10 years is: ", principal)


futurevalue()
futurevalue2()
futurevalue3()
