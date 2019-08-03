# exercise 5 - coffee shop sells at $10.50 plus shipping
#              each order ships at $.86 per pound + $1.50 fixed cost for overhead
#              calculate the cost of an order


def coffeeshipment():
    pounds = eval(input("How many pounds of coffee are you ordering? "))
    cost = (10.50 + .86) * pounds + 1.50
    print("Your order will cost a total of $", round(cost, 2))


coffeeshipment()
