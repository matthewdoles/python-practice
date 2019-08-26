

# exercise 1 - calculate total weekly wages given the number of hours and hourly wage
#              give time and a half for anything above 40
def wages():
    wage = eval(input("What is the hourly wage? "))
    hours = eval(input("How many hours were worked this week? "))
    total = wage * hours

    if hours > 40:
        overtime_pay = wage + (wage * .5)
        overtime_hours = hours - 40
        total += overtime_pay * overtime_hours

    print("You earned $", total)


wages()
