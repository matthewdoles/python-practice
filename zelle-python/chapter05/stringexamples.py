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
