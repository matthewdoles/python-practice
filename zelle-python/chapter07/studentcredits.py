# exercise 4 - determine a student's class based upon the number of completed credit hours
def studentclass():
    x = eval(input("How many credits do you have? "))

    if x < 7:
        print('Freshman')
    elif 7 <= x < 16:
        print('Sophomore')
    elif 16 <= x < 26:
        print('Junior')
    elif x >= 26:
        print('Senior')
    else:
        print("Please print a valid positive number ")


studentclass()
