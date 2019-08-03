# exercise 3 - find the molecular weight of a hydrocarbon given a number of hydrogen, carbon, and oxygen atoms
def molecularweight():
    h, c, o = eval(input("Enter the number of Hydrogen, Carbon, and Oxygen atoms separated by commas: "))
    weight = (h * 1.0079) + (c * 12.011) + (o + 15.9994)
    print("The molecular weigh of the hydrocarbon is", weight, "g/mol")


molecularweight()
