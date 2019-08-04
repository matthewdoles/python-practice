from graphics import *


# exercise 2 - draw an archery target, the width of each circle is equal
def target():
    win = GraphWin("Archery Target", 1000, 1000)
    win.setCoords(0.0, 0.0, 11.0, 11.0)
    center = Point(5.5, 5.5)

    c = Circle(center, 5)
    c.setOutline("black")
    c.setFill("white")
    c.setWidth(5)
    c.draw(win)

    c2 = Circle(center, 4)
    c2.setOutline("black")
    c2.setFill("red")
    c2.setWidth(5)
    c2.draw(win)

    c3 = Circle(center, 3)
    c3.setOutline("black")
    c3.setFill("blue")
    c3.setWidth(5)
    c3.draw(win)

    c4 = Circle(center, 2)
    c4.setOutline("black")
    c4.setFill("black")
    c4.setWidth(5)
    c4.draw(win)

    c5 = Circle(center, 1)
    c5.setOutline("black")
    c5.setFill("yellow")
    c5.setWidth(5)
    c5.draw(win)

    input("Press enter to exit")
    win.close()


target()
