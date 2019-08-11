str1 = "Hello"
str2 = "Matthew"
print(str1, str2)
# Hello Matthew

print(type(str1))
# <class 'str'>
print(type(str2))
# <class 'str'>

# strings are arrays
greet = "Hello Matthew"
print(greet[0])
# H
print(greet[0], greet[2], greet[4])
# H l o
x = 8
print(greet[x - 2])
# M

# can also index backwards
print(greet[-1])
# w
print(greet[-3])
# h

# slicing examples
print(greet[0:3])
# Hel
print(greet[5:9])
# Mat
print(greet[:5])
# Hello
print(greet[5:])
# Matthew
print(greet[:])
# Hello Matthew

# concatenation
concat = "spam" + "eggs"
print(concat)
# spameggs
concat = "Spam" + "And" + "Eggs"
print(concat)
# SpamAndEggs
concat = 3 * "spam"
print(concat)
# spamspamspam
concat = (3 * "spam") + (5 * "spam")
print(concat)
# spamspamspamspamspamspamspamspam
print(len("spam"))
# 4
for ch in "Spam!":
    print(ch, end="")
# Spam!
print()

# lists
print([1, 2] + [3, 4])
# [1, 2, 3, 4]
print([1, 2] * 3)
# [1, 2, 1, 2, 1, 2]
grades = ['A', 'B', 'C', 'D', 'F']
print(grades[0])
# A
print(grades[2:4])
# ['C', 'D']
print(len(grades))
# 5

# ordinal
print(ord("a"))
# 97
print(ord("A"))
# 65
print(chr(97))
# a
print(chr(90))
# Z

s = "hello, I came here for an argument"
print(s.capitalize())
# Hello, I came here for an argument
print(s.title())
# Hello, I Came Here For An Argument
print(s.lower())
# hello, i came here for an argument
print(s.upper())
# HELLO, I CAME HERE FOR AN ARGUMENT
print(s.replace("I", "you"))
# hello, you came here for an argument
print(s.center(30))
# hello, I came here for an argument
print(s.center(50))
#         hello, I came here for an argument
print(s.count('e'))
# 5
print(s.find(','))
# 5
print(" ".join(["Number", "one,", "the", "Larch"]))
# Number one, the Larch
print("spam".join(["Number", "one,", "the", "Larch"]))
# Numberspamone,spamthespamLarch

s = "Hello {0} {1}, you may have won ${2}".format("Mr.", "Smith", 10000)
# Hello Mr. Smith, you may have won $10000
print(s)
s = "This int, {0:5} was placed in a field of width 5".format(7)
print(s)
# This int,     7 was placed in a field of width 5
s = "This int, {0:10} was placed in a field of width 10".format(7)
print(s)
# This int,          7 was placed in a field of width 10
s = "This float, {0:10.5}, has width 10 and precision 5".format(3.1415926)
print(s)
# This float,     3.1416, has width 10 and precision 5
s = "This float, {0:10.5f}, is fixed at 5 decimal places".format(3.1415926)
print(s)
# This float,    3.14159, is fixed at 5 decimal places
s = "This float, {0:10.5f}, is fixed at 5 decimal places".format(3.1415926)
print(s)
# This float,    3.14159, is fixed at 5 decimal places
s = "This float, {0:0.5}, has width 0  and precision 5".format(3.1415926)
print(s)
# This float, 3.1416, has width 0  and precision 5
s = "Compare {0} and {0:0.20}".format(3.14)
print(s)
# Compare 3.14 and 3.1400000000000001243

s = "left justification: {0:<5}".format("Hi!")
print(s)
# left justification: Hi!
s = "right justification: {0:>5}".format("Hi!")
print(s)
# right justification:   Hi!
s = "centered: {0:^5}".format("Hi!")
print(s)
# centered:  Hi!
