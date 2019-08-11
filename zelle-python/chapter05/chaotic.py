

# exercise 11 - improve on the chaotic function from chapter 1 - print into formatted table
def chaotic():
    print("This Program illustrates a chaotic function\n")

    n = 10
    x = .25
    y = .26

    print("Index {0:>9}{1:>10}".format(x, y))
    print("--------------------------------")
    for i in range(n):
        x = 3.9 * x - 3.9 * x * x
        y = 3.9 * y - 3.9 * y * y
        print("{2:^3}{0:>12.5f}{1:>10.5f}".format(x, y, (i+1)))


chaotic()

# This Program illustrates a chaotic function
#
# Index      0.25      0.26
# --------------------------------
#  1      0.73125   0.75036
#  2      0.76644   0.73055
#  3      0.69814   0.76771
#  4      0.82190   0.69550
#  5      0.57089   0.82594
#  6      0.95540   0.56067
#  7      0.16619   0.96064
#  8      0.54042   0.14745
#  9      0.96863   0.49025
# 10      0.11851   0.97463
