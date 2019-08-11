def printfile():
    fname = input("Enter filename: ")
    infile = open(fname, "r")
    data = infile.read()
    print(data)


printfile()
# Enter filename: filetoprint.txt
# Print this file
# My name is Matthew
# I am learning Python
