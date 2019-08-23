# exercise 9 - alter exercise 3 from Chapter 5 into a function that calculates grade given score
def grade(score):
    if score < 60:
        print("Grade: F")
    if 60 <= score <= 69:
        print("Grade: D")
    if 70 <= score <= 79:
        print("Grade: C")
    if 80 <= score <= 89:
        print("Grade: B")
    if score >= 90:
        print("Grade: A")


grade(75)
# Grade: C
grade(55)
# Grade: F
grade(90)
# Grade: A
