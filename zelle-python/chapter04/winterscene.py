from graphics import *


# exercise 4 - create a program that draws a winter scene with a tree and snowman
def winterscene():
    win = GraphWin("Draw a Winter Scene", 500, 500)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    win.setBackground("lightblue")

    ground = Rectangle(Point(0, 0), Point(10, 3))
    ground.setFill("white")
    ground.draw(win)

    stump = Rectangle(Point(3, 3), Point(3.5, 3.5))
    stump.setFill("brown3")
    stump.draw(win)

    tree1 = Polygon(Point(2, 3.5), Point(4.5, 3.5), Point(3.25, 5))
    tree1.setFill("green4")
    tree1.draw(win)
    tree2 = Polygon(Point(2.25, 4.5), Point(4.25, 4.5), Point(3.25, 6))
    tree2.setFill("green4")
    tree2.draw(win)
    tree2 = Polygon(Point(2.5, 5.5), Point(4, 5.5), Point(3.25, 6.75))
    tree2.setFill("green4")
    tree2.draw(win)

    snowman1 = Circle(Point(6.5, 3.8), .8)
    snowman1.setFill("White")
    snowman1.setOutline("black")
    snowman1.draw(win)
    snowman2 = Circle(Point(6.5, 4.6), .6)
    snowman2.setFill("White")
    snowman2.setOutline("black")
    snowman2.draw(win)
    snowman3 = Circle(Point(6.5, 5.4), .4)
    snowman3.setFill("White")
    snowman3.setOutline("black")
    snowman3.draw(win)

    input("Press enter to exit")
    win.close()


winterscene()
