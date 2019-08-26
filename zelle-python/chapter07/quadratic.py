import math


def quadratic():
    print("This program finds the real solutions to a quadratic")
    print()

    a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
    discrim = b * b - 4 * a * c
    if discrim < 0:
        print("\nThe equation has no real roots.")
    elif discrim == 0:
        root = -b / (2 * a)
        print("There is a double root at", root)
    else:
        disc_root = math.sqrt(discrim)
        root1 = (-b + disc_root) / (2 * a)
        root2 = (-b - disc_root) / (2 * a)
        print("\nThe solutions are:", root1, root2)


def quadratic_exceptions():
    print("This program finds the real solutions to a quadratic")
    try:
        a, b, c = eval(input("\nPlease enter the coefficients (a, b, c): "))
        disc_root = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + disc_root) / (2 * a)
        root2 = (-b - disc_root) / (2 * a)
        print("\nThe solutions are:", root1, root2)
    except ValueError as excObj:
        if str(excObj) == "math domain error":
            print("No real roots")
        else:
            print("You didn't give the right number of coefficients.")
    except NameError:
        print("\nYou didn't enter three numbers.")
    except TypeError:
        print("Your inputs were not all numbers.")
    except SyntaxError:
        print("Your input was not in the correct comma separated format.")
    except:
        print("Something went wrong, sorry!")


quadratic()
