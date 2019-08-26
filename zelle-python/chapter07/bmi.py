# exercise 5 - determine a person's health using the BMI
def bodymassindex(weight, height):
    bmi = (weight * 720) / (height ** 2)
    return bmi


def main():
    weight, height = eval(input("What is your weight (in pounds) and height (in inches)?"))
    bmi = bodymassindex(weight, height)

    if 19 <= bmi <= 25:
        print("You are within the arbitrary healthy range.")
    elif bmi < 19:
        print("You are below the arbitrary healthy range.")
    elif bmi > 25:
        print("You are above the arbitrary healthy range.")
    else:
        print("Please enter a valid height and weight")


main()
