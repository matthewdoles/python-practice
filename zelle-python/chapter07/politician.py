

# exercise 8 - find out if a person is eligible to be a senator or representative
def eligibility():
    citizen = eval(input("How many years have you been a U.S. Citizen? "))
    age = eval(input("How old are you? "))
    if citizen >= 9:
        if age >= 30:
            print("You are eligible to serve as a U.S. Senator, or a member of the House.")
        elif 30 > age >= 25:
            print("You are eligible to run for the House of Representatives.")
        else:
            print("Sorry, but you are not eligible to serve as a congressional representative.")
    else:
        print("Sorry, but you are not eligible to serve as a congressional representative.")


eligibility()
