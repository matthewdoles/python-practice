from graphics import *


# exercise 11 - create a 5 click house
def fiveclickhouse():
    win = GraphWin("Welcome Home", 700, 700)
    win.setCoords(-10, -10, 10, 10)

    # two clicks for the frame of the house
    message = Text(Point(0, 8), "Click on 2 points to create the rectangular frame of your house.")
    message.draw(win)
    point1 = win.getMouse()
    point2 = win.getMouse()
    # save points for later calculations
    x1 = point1.getX()
    y1 = point1.getY()
    x2 = point2.getX()
    y2 = point2.getY()
    r = Rectangle(point1, point2)
    r.draw(win)
    message.undraw()

    # the third click will show the center of the top of the door
    # draw message below base of house
    message = Text(Point(0, y1 - 1), "Excellent! Click the top of the door frame.")
    message.draw(win)
    point3 = win.getMouse()
    x3 = point3.getX()
    y3 = point3.getY()
    # door width is 1/5 house width
    housewidth = x2 - x1
    door = Rectangle(Point(x3 - (1 / 10 * housewidth), y1), Point(x3 + (1 / 10 * housewidth), y3))
    door.draw(win)

    # click four will print a square window
    message.setText("Now click to place a window.")
    point4 = win.getMouse()
    x4 = point4.getX()
    y4 = point4.getY()
    # window is 1/2 width door (z is variable for distance off center)
    z = 1/20 * housewidth
    window = Rectangle(Point((x4 - z), (y4 - z)), Point((x4 + z), (y4 + z)))
    window.draw(win)

    # click five will indicate peak of roof
    message.setText("Click for the peak of the roof!")
    point5 = win.getMouse()
    line1 = Line(point2, point5)
    line1.draw(win)
    line2 = Line(point5, Point(x1, y2))
    line2.draw(win)

    message.setText("Welcome, to your new home. Click anywhere to close.")
    win.getMouse()
    win.close()


fiveclickhouse()
