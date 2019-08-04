from graphics import *


def futval():
    print("This program plots the growth of a 10-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annualized interest rate: "))

    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    Text(Point(20, 230), ' 0.0K').draw(win)
    Text(Point(20, 180), ' 2.5K').draw(win)
    Text(Point(20, 130), ' 5.0K').draw(win)
    Text(Point(20, 80), ' 7.5K').draw(win)
    Text(Point(20, 30), ' 10.0K').draw(win)

    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230 - height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    for year in range(1, 11):
        principal = principal * (1 + apr)
        xll = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(xll, 230), Point(xll + 25, 230 - height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    input("Press enter to exit")
    win.close()


def futval_coords():
    print("This program plots the growth of a 10-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annualized interest rate: "))

    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    win.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1, 0), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5K').draw(win)
    Text(Point(-1, 10000), ' 10.0K').draw(win)

    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    for year in range(1, 11):
        principal = principal * (1 + apr)
        bar = Rectangle(Point(year, 0), Point(year + 1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    input("Press enter to exit")
    win.close()


# exercise 6 - alter so that the inputs are also done in the graphic
def futval_entry():

    print("This program plots the growth of a 10-year investment.")
    win = GraphWin("Investment Growth Chart", 500, 500)
    win.setBackground("white")
    win.setCoords(-1.75, -200, 11.5, 10400.0)

    Text(Point(1, 8000), "Initial Principal:").draw(win)
    Text(Point(1, 6000), "Interest Rate:").draw(win)
    input1 = Entry(Point(5, 8000), 5)
    input1.setText("0")
    input1.draw(win)
    input2 = Entry(Point(5, 6000), 5)
    input2.setText("0")
    input2.draw(win)

    output = Text(Point(2, 1), "")
    output.draw(win)
    button = Text(Point(5, 3750), "Graph It")
    button.draw(win)
    Rectangle(Point(4, 3000), Point(6, 4500)).draw(win)

    win.getMouse()
    win.close()

    principal = eval(input1.getText())
    apr = eval(input2.getText())


    win = GraphWin("Investment Growth Chart", 700, 700)
    win.setBackground("white")
    win.setCoords(-1.75, -200, 11.5, 10400)

    Text(Point(-1, 0), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5K').draw(win)
    Text(Point(-1, 10000), ' 10.0K').draw(win)

    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    for year in range(1, 11):
        principal = principal * (1 + apr)
        bar = Rectangle(Point(year, 0), Point(year + 1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    input("Press enter to exit")
    win.close()


futval_entry()
