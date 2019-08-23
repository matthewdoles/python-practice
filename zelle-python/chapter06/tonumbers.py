# exercise 13 - write a fuction that converts string into numbers (integers)
def tonumbers(convert):
    for x in range(len(convert)):
        convert[x] = int(convert[x])


def main():
    x = ['1','2','3','4','5']
    tonumbers(x)
    print(x)
    # [1, 2, 3, 4, 5]


main()
