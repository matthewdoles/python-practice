# for loops - reading from a file
def avg5():
    fname = input("What files are the numbers in? ")
    infile = open(fname, 'r')

    sum = 0.0
    count = 0
    for line in infile:
        sum = sum + eval(line)
        count = count + 1
    print("\nThe average of the numbers is", sum / count)


avg5()
