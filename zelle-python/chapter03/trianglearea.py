import math


# exercise 9 - calculate the area of a triangle give sides a, b, and c
def trianglearea():
    a, b, c = eval(input("What are the lengths of side a, b, and c? "))
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("The area of the triangle is", round(area, 2))


trianglearea()
