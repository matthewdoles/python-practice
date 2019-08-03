

# exercise 16 - find the nth term of a Fibonacci sequence
def fibonacci():
    n = eval(input("What number in the Fibonacci sequence would you like to see?: "))
    x = 1
    y = 0
    sequence = []

    for i in range(n):
        z = x + y
        sequence.append(z)
        y = x
        x = z
        print(sequence)

    print("Position", n, "equals", z, "in the Fibonacci sequence")


fibonacci()
