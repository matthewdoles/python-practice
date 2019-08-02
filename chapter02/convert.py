# a program to convert Celsius temps to Fahrenheit
def celsiustofahrenheit1():
    # exercise 1 - print an intro for this program
    print("Ths program converts Celsius to Fahrenheit")
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")


# exercise 3 - alter to execute 5 times instead of 1
def celsiustofahrenheit2():
    print("Ths program converts Celsius to Fahrenheit")
    for i in range(5):
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")


# exercise 4 - alter to print the conversion from 0C to 100C incrementally by 10
def celsiustofahrenheit3():
    print("Ths program converts Celsius to Fahrenheit")
    for i in range(0, 101, 10):
        fahrenheit = 9/5 * i + 32
        print(i, "C =", fahrenheit, "F")


# exercise 8 - write convert.py backwards to convert Fahrenheit to Celsius
def celsiustofahrenheit4():
    print("Ths program converts Fahrenheit to Celsius")
    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = 5/9 * (fahrenheit - 32)
    print("The temperature is", celsius, "degrees Fahrenheit.")


# exercise 9 - write a program to convert kilometers to miles
def kilometerstomiles():
    print("Ths program converts kilometers to miles")
    kilometers = eval(input("What is the distance in kilometers? "))
    miles = kilometers * 0.62
    print(kilometers, "kilometers is", miles, "miles")


celsiustofahrenheit1()
celsiustofahrenheit2()
celsiustofahrenheit3()
celsiustofahrenheit4()
kilometerstomiles()
