# while loops - reading from a file
def avg6():
    fname = input("What files are the numbers in? ")
    infile = open(fname, 'r')

    sum = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        sum = sum + eval(line)
        count = count + 1
        line = infile.readline()
    print("\nThe average of the numbers is", sum / count)


avg6()
