# program to average two exam scores
# demonstrates use of multiple input


def avgtwonumbers():
    print("This program computes the average of two exam scores.")
    score1, score2 = eval(input("Enter two scores separated by a comma: "))
    average = (score1 + score2) / 2
    print("The average of the two scores is:", average)


# exercise 2 - alter to find the average of three scores
def avgthreenumbers():
    print("This program computes the average of three exam scores.")
    score1, score2, score3 = eval(input("Enter three scores separated by a comma: "))
    average = (score1 + score2 + score3) / 3
    print("The average of the three scores is:", average)


avgtwonumbers()
avgthreenumbers()

