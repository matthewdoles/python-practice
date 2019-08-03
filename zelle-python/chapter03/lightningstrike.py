# exercise 4 - determine the distance to a lightning strike based upon time elapsed since flash and sound
def lightning():
    time = eval(input("What was the elapsed time (in seconds) between the flash and sound of thunder: "))
    distance = (time * 1100) / 5280
    print("The lightning strike was", distance, "miles away.")


lightning()
