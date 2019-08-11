def texttounicode():
    print("This program converts a textual message into a sequence", end="")
    print("of numbers representing the Unicode encoding")

    message = input("Please enter the message to encode: ")

    print("Here is the message encoded in Unicode")
    for ch in message:
        print(ord(ch), end=" ")
    print()


def unicodetotext():
    print("This program converts a sequence of Unicode numbers into", end="")
    print("the string of text that it represents.\n")

    in_string = input("Please enter the Unicode-encoded message: ")

    chars = []
    for numStr in in_string.split():
        code_num = eval(numStr)             # converts digits to number
        chars.append(chr(code_num))   # converts number into character and append to message
    message = "".join(chars)
    print(message)


texttounicode()
unicodetotext()

