

# exercise 7 - Caesar cipher, shift the letters of a message by a fixed value
def caesarcipher():
    p_text = input("Enter the message you'd like encrypted: ")
    key = eval(input("What's the numeric key: "))

    c_text = ""
    for ch in p_text:
        c_text = c_text + (chr(ord(ch) + key))

    print("Your encoded message is {0}.".format(c_text))


# exercise 7 - improve Caesar cipher so that if it shits past z it circles back to a
def caesarcipher2():
    p_text = input("Enter the message you'd like encrypted: ")
    key = eval(input("What's the numeric key: "))

    c_text = ""
    for ch in p_text:
        if (ord(ch) + key) > 122:
            temp = (ord(ch) + key) - 122
            c_text = c_text + (chr(96 + temp))
        else:
            c_text = c_text + (chr(ord(ch) + key))

    print("Your encoded message is {0}.".format(c_text))


caesarcipher2()
