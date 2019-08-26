from graphics import *
import math


# exercise 14 - redo exercise 7 from chapter 4 to handle when line does not intersect circle
def main():
    win = GraphWin("Intersection of a line through a Circle", 500, 500)
    win.setCoords(-10, -10, 10, 10)

    r = eval(input("What is the radius of the circle? "))
    y = eval(input("Where does the line cross the y axis? "))

    c = Circle(Point(0, 0), r)
    c.draw(win)

    line = Line(Point(-10, y), Point(10, y))
    line.draw(win)

    if r < y:
        print("The line does not intersect.")
    else:
        x = math.sqrt(r**2 - y**2)
        print(-x, x)

        x1 = Text(Point(-x, y + 2), -x)
        x2 = Text(Point(x, y + 2), x)
        x1.draw(win)
        x2.draw(win)


main()
