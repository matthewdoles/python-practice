import math


# exercise 2 - finds the price per sq in of a pizza given price and diameter
def pizza():
    print("This program finds the price per square inch of a pizza given a price and diameter")
    print()

    price = eval(input("Please enter the pizza's price: "))
    d = eval(input("Please enter the pizza's diameter: "))
    area = math.pi * ((d / 2) ** 2)
    p = price / area

    print()
    print("The price per square inch of this pizza is $", round(p, 2), "you nerd.")


pizza()
