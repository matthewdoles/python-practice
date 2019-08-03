import math


# exercise 6 - find the slope of a line given two (non-vertical) points by the user
def lineslope():
    x1,y1 = eval(input("First point x,y: "))
    x2, y2 = eval(input("Second point x,y: "))
    slope = (y2 - y1) / (x2 - x1)
    print("The slope of the line for these two points is", slope)


# exercise 6 - find the distance of a line given two points by the user
def linedistance():
    x1, y1 = eval(input("First point x,y: "))
    x2, y2 = eval(input("Second point x,y: "))
    distance = math.sqrt(((y2 - y1) ** 2) + ((x2 - x1) ** 2))
    print("The distance between these two points is", distance)


lineslope()
linedistance()