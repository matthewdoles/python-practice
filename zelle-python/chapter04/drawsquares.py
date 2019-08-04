from graphics import *


# exercise 1 - with each successive click draw a square, (do 10 times then click to close)
def drawsquare():
    win = GraphWin("Draw Squares", 700, 700)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    square = Rectangle(Point(4, 4), Point(6, 6))
    square.setOutline("red")
    square.setFill("red")
    square.draw(win)

    for i in range(10):
        p = win.getMouse()
        c = square.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        new = square.clone()
        new.draw(win)
        new.move(dx, dy)
        square = new

    message = Text(Point(5, 9), "Click anywhere to close")
    message.draw(win)
    win.getMouse()
    win.close()


drawsquare()
