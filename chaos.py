# standard chaos function
def chaos():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)


# chaos function where x is changed to 2.0
def chaos2():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(20):
        x = 2.0 * x * (1 - x)
        print(x)


# chaos function where user defines number of printed numbers
def chaos3():
    print("This program illustrates a chaotic function")
    n = eval(input("How many numbers should I print? "))
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        print(x)


# chaos function re-writing the same formula in various ways
def chaos4():
    print("Ths program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    a = x
    b = x
    c = x
    for i in range(100):
        a = 3.9 * a * (1 - a)
        b = 3.9 * b * (b - b * b)
        c = 3.9 * c - 3.9 * c * c
        print("{0:<30.20}{1:<30.20}{2:<30.20}".format(a, b, c))


# chaos function that takes two inputs and prints into formatted table
def chaos5():
    print("Ths program illustrates a chaotic function")
    x = float(input("Enter first number between 0 and 1: "))
    y = float(input("Enter second number between 0 and 1: "))
    z = "input"
    print("{2:<8}{0:<13.2f}{1:<6.2f}".format(x, y, z))
    print("---------------------------")
    for i in range(10):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print("{0:>14.6f}{1:>13.6f}".format(x, y))


chaos()
chaos2()
chaos3()
chaos4()
chaos5()