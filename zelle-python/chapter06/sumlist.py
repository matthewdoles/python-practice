# exercise 12 - write a function that sums all numbers in a list
def sumlist(numbers):
    x = 0
    for i in range(len(numbers)):
        x += numbers[i]
    return x


def main():
    a = [2, 4, 15, 100]
    print(sumlist(a))
    # 121
    b = [5, 7, 25]
    print(sumlist(b))
    # 37
    c = [1, 1, 1]
    print(sumlist(c))
    # 3


main()
