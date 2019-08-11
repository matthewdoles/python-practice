

# exercise 14 - common small program in unix/linux systems; count lines, words, and characters
def wc():
    fname = input("Enter filename: ")
    infile = open(fname, "r")

    line_count = 0
    word_count = 0
    char_count = 0

    for line in infile:
        line_count += 1
        words = line.split()
        word_count = word_count + len(words)
        for word in words:
            for char in word:
                char_count += 1

    infile.close()

    print("\nThere are {0} lines in the file.".format(line_count))
    print("The total number of letters is {0}".format(char_count))
    print("The number of words is {0}".format(word_count))


wc()
# Enter filename: names.txt
#
# There are 5 lines in the file.
# The total number of letters is 53
# The number of words is 10
