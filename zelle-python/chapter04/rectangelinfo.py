from graphics import *
import math


# exercise 8 - user draws a rectangle, display information about that line
def rectangleinfo():
    win = GraphWin("Draw a Rectangle", 1000, 1000)
    win.setCoords(-10, -10, 10, 10)
    message = Text(Point(0, 9.5), "Click on two points to draw a Rectangle")
    message.draw(win)

    p1 = win.getMouse().draw(win)
    p2 = win.getMouse().draw(win)

    rectangle = Rectangle(p1, p2)
    rectangle.setFill("orange2")
    rectangle.draw(win)

    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()

    area = abs((x2 - x1) * (y2 - y1))
    message = "Area:", area
    output = Text(Point(0, 9), message)
    output.draw(win)

    perimeter = 2 * ((x2 - x1) + (y2 - y1))
    message = "Perimeter:", perimeter
    output = Text(Point(0, 8.5), message)
    output.draw(win)

    message = Text(Point(0, 8), "Click anywhere to close")
    message.draw(win)
    win.getMouse()
    win.close()


rectangleinfo()
