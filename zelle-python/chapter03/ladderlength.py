import math


# exercise 10 - find the length of the ladder needed to reach a height given that height and angle of ladder
def ladderlength():
    height = eval(input("What is the height you are trying to reach in feet? "))
    angle = eval(input("What is the angle the ladder is being placed in degrees? "))
    length = height / math.sin(angle)
    print("The length of the ladder needs to be", length, "feet")


ladderlength()
