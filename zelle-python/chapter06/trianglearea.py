import math
from graphics import *


# exercise 6 - augment triangle area exercise from Chapter 3 so area calculation is a function
def area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def square(x):
    return x * x


def distance(p1, p2):
    dist = math.sqrt(square(p2.getX() - p1.getX()) + square(p2.getY() - p1.getY()))
    return dist


def triangle():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    triangle = Polygon(p1, p2, p3)
    triangle.setFill("blue")
    triangle.setOutline("black")
    triangle.draw(win)

    a = area(distance(p1, p2), distance(p2, p3), distance(p3, p1))
    message.setText("The area is: {0:0.2f}".format(a))

    win.getMouse()
    win.close()


triangle()
