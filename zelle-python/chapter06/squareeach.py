# exercise 11 - write a function that square each number in a list
def squarelist(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * numbers[i]


def main():
    nums = [2, 4, 15, 100]
    squarelist(nums)
    print(nums)


main()
# [4, 16, 225, 10000]
