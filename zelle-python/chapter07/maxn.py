def maxn():
    n = eval(input("How many numbers are there? "))
    max = eval(input("Enter a number>> "))
    for i in range(n - 1):
        x = eval(input("Enter a number>> "))
        if max < x:
            max = x
    print("The largest value is", max)


maxn()