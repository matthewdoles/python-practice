#exericse 1 - print the lyrics of old mcdonald
def verse1():
    print("Old McDonald had a farm Ee-igh, Ee-igh, Oh!")


def verse2(animal):
    print("And on that farm he had a", animal, "Ee-igh, Ee-igh, Oh!")


def verse3(noise):
    print("With a", noise + ",", noise, "here and a", noise + ",", noise + " there.")
    print("Here a", noise + ", there a", noise, "everywhere a", noise + ",", noise + ".")


def oldmcdonald():
    verse1()
    verse2("cow")
    verse3("moo")
    verse1()
    print()
    verse1()
    verse2("pig")
    verse3("oink")
    verse1()


oldmcdonald()
# Old McDonald had a farm Ee-igh, Ee-igh, Oh!
# And on that farm he had a cow Ee-igh, Ee-igh, Oh!
# With a moo, moo here and a moo, moo there.
# Here a moo, there a moo everywhere a moo, moo.
# Old McDonald had a farm Ee-igh, Ee-igh, Oh!
#
# Old McDonald had a farm Ee-igh, Ee-igh, Oh!
# And on that farm he had a pig Ee-igh, Ee-igh, Oh!
# With a oink, oink here and a oink, oink there.
# Here a oink, there a oink everywhere a oink, oink.
# Old McDonald had a farm Ee-igh, Ee-igh, Oh!
