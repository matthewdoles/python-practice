

# exercise 9 - fuel efficiency, calculate the mpg for each leg and avg mpg using odometer and total gas
def legcalculator(start_odom):
    count = 0
    leg = ""
    total_gas = 0
    total_distance = 0
    leg = input("Enter the current odometer and amount of gas (gallons) for this leg, "
                "\nseparated by a space (<Enter> to quit)>> ")
    while leg != "":
        odom, gas = leg.split(" ")
        odom = eval(odom)
        gas = eval(gas)

        count = count + 1
        distance = odom - start_odom
        start_odom = odom
        leg_mpg = distance / gas

        print("On leg {0}, you got {1}/gal.".format(count, round(leg_mpg, 2)))

        total_distance = total_distance + distance
        total_gas = total_gas + gas

        leg = input("Enter the current odometer and amount of gas (gallons) for this leg, "
                    "\nseparated by a space (<Enter> to quit)>> ")

    return total_gas, total_distance


def main():
    odom = int(input("What is your current odometer reading: "))
    gas, distance = legcalculator(odom)

    avg_mpg = distance / gas
    print("On this whole trip, you averaged {0}/gal.".format(round(avg_mpg, 2)))


main()
