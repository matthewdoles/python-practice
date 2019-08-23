import math


# exercise 3 - create functions to calculate sphere surface area and volume
def volume(radius):
    return (4 / 3) * math.pi * (radius ** 3)


def surfacearea(radius):
    return 4 * math.pi * (radius ** 2)


def sphere():
    print("This program finds the volume and surface area of a sphere given a radius")
    print()

    r = eval(input("Please enter the sphere's radius: "))
    v = volume(r)
    sa = surfacearea(r)
    print()
    print("The volume is:", v)
    print("The surface area  is:", sa)


sphere()
# This program finds the volume and surface area of a sphere given a radius
#
# Please enter the sphere's radius: 10
#
# The volume is: 4188.790204786391
# The surface area  is: 1256.6370614359173
