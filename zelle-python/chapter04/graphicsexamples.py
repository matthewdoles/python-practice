from graphics import *


def graph():
    win = GraphWin()
    p = Point(50, 60)
    p.draw(win)
    p2 = Point(140, 100)
    p2.draw(win)
    input("Press enter to exit")
    win.close()


def graphshapes():
    win = GraphWin('Shapes')
    center = Point(100, 100)
    circle = Circle(center, 30)
    circle.setFill('red')
    circle.draw(win)
    label = Text(center, "Red Circle")
    label.draw(win)
    rect = Rectangle(Point(30, 30), Point(70, 70))
    rect.draw(win)
    line = Line(Point(20, 30), Point(180, 165))
    line.draw(win)
    oval = Oval(Point(20, 150), Point(180, 199))
    oval.draw(win)
    input("Press enter to exit")
    win.close()


def createtwocircles():
    win = GraphWin('Two Circles')
    left_eye = Circle(Point(80, 50), 5)
    left_eye.setFill('yellow')
    left_eye.setOutline('red')
    left_eye.draw(win)
    right_eye = Circle(Point(100, 50), 5)
    right_eye.setFill('yellow')
    right_eye.setOutline('red')
    right_eye.draw(win)
    input("Press enter to exit")
    win.close()


def tictactoe():
    win = GraphWin("Tic-Tac-Toe", 300, 300)
    win.setCoords(0.0, 0.0, 3.0, 3.0)
    Line(Point(1, 0), Point(1, 3)).draw(win)
    Line(Point(2, 0), Point(2, 3)).draw(win)
    Line(Point(0, 1), Point(3, 1)).draw(win)
    Line(Point(0, 2), Point(3, 2)).draw(win)
    input("Press enter to exit")
    win.close()


graph()
graphshapes()
createtwocircles()
tictactoe()
