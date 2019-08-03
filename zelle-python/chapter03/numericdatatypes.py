import math


def main():
    print(type(3))
    # <class 'int'>

    print(type(3.14))
    # <class 'float'>

    print(type(3.0))
    # <class 'float'>

    print(type(-32))
    # <class 'int'>

    print(type(32.0))
    # <class 'float'>

    print(3 + 4)
    # <class 'int'> - 7

    print(3.0 + 4.0)
    # <class 'float'> - 7.0

    print(3 * 4)
    # <class 'int'> - 12

    print(3.0 * 4.0)
    # <class 'float'> - 12.0

    print(4 ** 3)
    # <class 'int'> - 64

    print(4.0 ** 3)
    # <class 'float'> - 64.0

    print(abs(5))
    # <class 'int'> - 5

    print(abs(-3.5))
    # <class 'float'> - 3.5

    print(10 / 3)
    # <class 'float'> - 3.333333

    print(10.0 / 3.0)
    # <class 'float'> - 3.333333

    print(10 / 5)
    # <class 'float'> - 2.0

    print(10 // 3)
    # <class 'int'> - 3

    print(10.0 // 3.0)
    # <class 'float'> - 3.0

    print(10 % 3)
    # <class 'int'> - 1

    print(10.0 % 3.0)
    # <class 'float'> - 1.0

    print(round(math.pi, 2))
    # <class 'float'> - 3.14

    print(round(math.pi, 3))
    # <class 'float'> - 3.142


main()
