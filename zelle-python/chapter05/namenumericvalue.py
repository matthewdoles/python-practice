

# exercise 5 - find the numeric sum of a peron's name: a = 1, b = 2, c = 3, ....
def numericvalue():
    name = input("What is your name? ")
    name = name.lower()

    sum = 0
    for ch in name:
        sum = int(ord(ch)) + sum - 96

    print("The numeric sum of your name is {0}.".format(sum))


# exercise 6 - find the numeric sum of a person's entire name
# note: does not account for special characters like - or '
def fullname():
    name = input("What is your name? ")
    name = name.lower().replace(" ", "")

    sum = 0
    for ch in name:
        sum = int(ord(ch)) + sum - 96

    print("The numeric sum of your name is {0}.".format(sum))


numericvalue()
fullname()