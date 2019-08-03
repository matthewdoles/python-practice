from graphics import *


def click():
    win = GraphWin("Click Me!")
    for i in range(10):
        p = win.getMouse()
        print("You clicked at:", p.getX(), p.getY())

    input("Press enter to exit")
    win.close()


def drawtriangle():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    p1 = win.getMouse().draw(win)
    p2 = win.getMouse().draw(win)
    p3 = win.getMouse().draw(win)

    triangle = Polygon(p1, p2, p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    input("Press enter to exit")
    win.close()


def convert():
    win = GraphWin("Celsius Converter", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    Text(Point(1, 3), "   Celsius Temperature:").draw(win)
    Text(Point(1, 1), "Fahrenheit Temperature:").draw(win)
    input = Entry(Point(2, 3), 5)
    input.setText("0.0")
    input.draw(win)
    output = Text(Point(2, 1), "").draw(win)
    button = Text(Point(1.5, 2.0), "Convert It").draw(win)

    win.getMouse()
    celsius = eval(input.getText())
    fahrenheit = 9.0 / 5.0 * celsius + 32

    output.setText(fahrenheit)
    button.setText("Quit")
    win.getMouse()
    win.close()


click()
drawtriangle()
convert()
