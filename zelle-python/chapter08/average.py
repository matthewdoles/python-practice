# for loop - average example
def avg():
    n = eval(input("How many numbers will be entered? "))
    sum = 0.0
    for i in range(n):
        x = eval(input("Enter a number >> "))
        sum = sum + x

        current_avg = sum / (i + 1)
        print("Current average", current_avg)

    print()
    print("Final average", sum / n)


avg()
