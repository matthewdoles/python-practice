

# exercise 9 - count the number of words in a sentence
def countwords():
    sentence = input("Please enter a sentence: ")
    words = 0
    for string in sentence.split():
        words += 1

    print("This sentence has {0} words.".format(words))


# exercise 10 - find the average length of a word in a sentence
def wordlengthaverage():
    sentence = input("Please enter a sentence: ")
    sum = 0
    words = 0
    for string in sentence.split():
        words += 1
        for char in string:
            sum += 1

    print("This sentence has {0} words.".format(words))
    print("The average length of a word in this sentence is {0}".format(sum / words))


countwords()
wordlengthaverage()
