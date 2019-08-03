import math


# exercise 1 - find the volume of a sphere
def spherevolume():
    print("This program finds the volume of a sphere given a radius")
    print()

    r = eval(input("Please enter the sphere's radius: "))
    volume = (4 / 3) * math.pi * (r ** 3)

    print()
    print("The volume is:", volume)


# exercise 1 - find the surface area of a sphere
def spheresurfacearea():
    print("This program finds the surface area of a sphere given a radius")
    print()

    r = eval(input("Please enter the sphere's radius: "))
    volume = 4 * math.pi * (r ** 2)

    print()
    print("The volume is:", volume)


spherevolume()
spheresurfacearea()
