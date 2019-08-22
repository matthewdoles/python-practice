import math
from graphics import *


def square(x):
    return x * x


print(square(3))
# 9
x = 5
y = square(x)
print(y)
# 25
print(square(x) + square(3))
# 34


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

    perim = distance(p1, p2) + distance(p2, p3) + distance(p3, p1)
    message.setText("The perimeter is: {0:0.2f}".format(perim))

    win.getMouse()
    win.close()


def sumdiff(x ,y):
    sum = x + y
    diff = x - y
    return sum, diff


print(sumdiff(5, 4))
# (9, 1)
s, d = sumdiff(17, 7)
print("Sum:", s, " Diff:", d)
# Sum: 24  Diff: 10

triangle()
