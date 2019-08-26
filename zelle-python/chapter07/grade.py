

# exercise 2 - find the score for a five point quiz, use if-else logic
def fivepointquiz():
    x = eval(input("What is the number grade? "))
    if x == 5:
        print('A')
    elif x == 4:
        print('B')
    elif x == 3:
        print('C')
    elif x == 2:
        print('D')
    elif x == 1:
        print('F')
    elif x == 0:
        print('F')
    else:
        print('Please enter an integer between 0 and 5')


def exams():
    x = eval(input("What is the number grade? "))
    if x >= 90:
        print('A')
    elif 90 > x >= 80:
        print('B')
    elif 80 > x >= 70:
        print('C')
    elif 70 > x >= 60:
        print('D')
    elif 60 > x:
        print('F')
    else:
        print('Please enter an integer between 0 and 100')


fivepointquiz()
exams()
