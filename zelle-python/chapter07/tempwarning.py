def tempwarning():
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9 / 5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

    if fahrenheit > 90:
        print("It's a hot one out there, be careful!")
    if fahrenheit < 30:
        print("Brrrr.  Be sure to dress warmly.")


tempwarning()
