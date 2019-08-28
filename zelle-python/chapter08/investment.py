

# exercise 3 - find the amount of years it will take for an investment to double given an interest rate
def main():
    rate = eval(input("What is the interest rate for the investment? "))
    # arbitrary, investment will double in same time no matter the amount
    investment = 100
    year = 0
    while investment < 200:
        investment = investment + (investment * rate)
        year = year + 1

    print("An investment would take", year, "years to double at an interest rate of", rate)


main()
# What is the interest rate for the investment? .25
# An investment would take 4 years to double at an interest rate of 0.25

# What is the interest rate for the investment? 1
# An investment would take 1 years to double at an interest rate of 1

# What is the interest rate for the investment? .05
# An investment would take 15 years to double at an interest rate of 0.05
