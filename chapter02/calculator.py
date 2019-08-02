# exercise 11 - write an interactive calculator program, run 100 times or til user exits
def calculator():
    for i in range(100):
        operation = input('''
        Please enter the operation you would like to do:
        + for Addition
        - for Subtraction
        * for Multiplication
        / for Division
        ''')

        number_1 = eval(input('Please enter the first number: '))
        number_2 = eval(input('Please enter the second number: '))

        if operation == '+':
            print('{} + {} = '.format(number_1, number_2), end="")
            print(number_1 + number_2)
        if operation == '-':
            print('{} - {} = '.format(number_1, number_2), end="")
            print(number_1 - number_2)
        if operation == '*':
            print('{} * {} = '.format(number_1, number_2), end="")
            print(number_1 * number_2)
        if operation == '/':
            print('{} / {} = '.format(number_1, number_2), end="")
            print(number_1 / number_2)
        else:
            print('Invalid operation, please run the program again.')


calculator()