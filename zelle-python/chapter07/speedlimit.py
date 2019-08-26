

# exercise 6 - calculate speeding fine, $50 inital fee, $5 for each MPH over, and additional $200 for over 90 MPH
def main():
    speedlimit = eval(input("Please report speed: "))
    actual = eval(input("What is the reported speed limit: "))

    diff = actual - speedlimit
    if diff >= 0:
        fine = (diff * 5) + 50
        if actual >= 90:
            fine = fine + 200
        print("You owe ${0}.".format(fine))
    elif diff < 0:
        print("No speeding violation committed.")
    else:
        print("Check the speed limit or reported speed.")


main()
