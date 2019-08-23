# exercise 10 - alter exercise 5 from Chapter 5 into a function that return acronym for a phrase
def acronym(phrase):
    words = []
    for string in phrase.split():
        words.append(string[0].upper())

    return "".join(words)


print("Acronym:", acronym("Johnson & Johnson"))
# Acronym: J&J
print("Acronym:", acronym("Matthew Edward Doles"))
# Acronym: MED
print("Acronym:", acronym("ABC ABC CBA"))
# Acronym: AAC
