

# exercise 4 - user enters a phrase, output the acronym of that phrase
def acronym():
    phrase = input("What words would you like an acronym for? ")

    words = []
    for string in phrase.split():
        words.append(string[0].upper())

    print("Acronym:", "".join(words))


acronym()