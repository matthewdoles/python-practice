def happy():
    print("Happy birthday to you!")


def singMatthew():
    happy()
    happy()
    print("Happy birthday, dear Matthew")
    happy()


def singPerson(person):
    happy()
    happy()
    print("Happy birthday, dear", person + ".")
    happy()


singMatthew()
print()
singPerson("Dan")
# Happy birthday to you!
# Happy birthday to you!
# Happy birthday, dear Matthew
# Happy birthday to you!
#
# Happy birthday to you!
# Happy birthday to you!
# Happy birthday, dear Dan.
# Happy birthday to you!
