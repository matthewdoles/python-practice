from graphics import *


# exercise 3 - create a program that draws some sort of face
def drawface():
    win = GraphWin("Draw a Face", 500, 500)
    win.setCoords(0.0, 0.0, 11.0, 11.0)
    head = Circle(Point(5.5, 5.5), 5)
    head.setOutline("black")
    head.draw(win)

    eye1 = Circle(Point(7.5, 7), 1)
    eye1.setOutline("black")
    eye1.draw(win)
    eye2 = Circle(Point(3.5, 7), 1)
    eye2.setOutline("black")
    eye2.draw(win)

    mouth = Rectangle(Point(3, 3), Point(8, 4))
    mouth.draw(win)

    input("Press enter to exit")
    win.close()


drawface()

