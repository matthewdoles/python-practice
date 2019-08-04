from graphics import *
import math


# exercise 8 - user draws a line, display information about that line
def linesegment():
    win = GraphWin("Draw a Line", 1000, 1000)
    win.setCoords(-10, -10, 10, 10)
    message = Text(Point(0, 9.5), "Click on two points to draw a line")
    message.draw(win)

    p1 = win.getMouse().draw(win)
    p2 = win.getMouse().draw(win)

    line = Line(p1, p2)
    line.draw(win)

    dx = p2.getX() - p1.getY()
    dy = p2.getY() - p1.getY()

    slope = dy / dx
    message = "Slope:", slope
    output = Text(Point(0, 9), message)
    output.draw(win)

    length = math.sqrt((dx ** 2) + (dy ** 2))
    message = "Length:", length
    output = Text(Point(0, 8.5), message)
    output.draw(win)

    message = Text(Point(0, 8), "Click anywhere to close")
    message.draw(win)
    win.getMouse()
    win.close()


linesegment()
