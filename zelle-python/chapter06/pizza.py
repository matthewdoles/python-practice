import math


# exercise 5 - redo pizza exercise from Chapter 3 using functions
def area(d):
    return math.pi * ((d / 2) ** 2)


def price(price, area):
    return price / area


def pizza():
    print("This program finds the price per square inch of a pizza given a price and diameter")
    print()

    p = eval(input("Please enter the pizza's price: "))
    d = eval(input("Please enter the pizza's diameter: "))
    a = area(d)
    price_sq_inch = price(p, a)

    print()
    print("The price per square inch of this pizza is $", round(price_sq_inch, 2), "you nerd.")


pizza()
# This program finds the price per square inch of a pizza given a price and diameter
#
# Please enter the pizza's price: 10
# Please enter the pizza's diameter: 12
#
# The price per square inch of this pizza is $ 0.09 you nerd.
