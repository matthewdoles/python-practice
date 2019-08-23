

# exercise 14 - user previous three functions (square, sum, and convert) to
#               read a file, convert strings into numbers, square each number, and add them
def tonumbers(convert):
    for x in range(len(convert)):
        convert[x] = int(convert[x])


def squarelist(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * numbers[i]


def sumlist(numbers):
    x = 0
    for i in range(len(numbers)):
        x += numbers[i]
    return x


def main():
    fname = input("Enter filename: ")
    infile = open(fname, "r")

    x = []
    for line in infile.readlines():
        x.append(line)

    tonumbers(x)
    squarelist(x)
    y = sumlist(x)
    print("Sum:", y)

    infile.close()


main()
# Enter filename: compute_file_test.txt
# Sum: 55
