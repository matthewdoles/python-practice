

# exercise 2 - 5 point quizzes grade from a 0 to 5 scale
def fivepointquiz():
    correct = eval(input("How many questions for this quiz were correct? "))
    grade = ["F", "F", "D", "C", "B", "A"]
    print("Grade:", grade[correct])


# exercise 3 - 100 point test that are graded on a standard A to F scale
def testgrade():
    percentage = eval(input("What was the grade percentage for this test? "))
    if percentage < 60:
        print("Grade: F")
    if 60 <= percentage <= 69:
        print("Grade: D")
    if 70 <= percentage <= 79:
        print("Grade: C")
    if 80 <= percentage <= 89:
        print("Grade: B")
    if percentage >= 90:
        print("Grade: A")


fivepointquiz()
testgrade()
