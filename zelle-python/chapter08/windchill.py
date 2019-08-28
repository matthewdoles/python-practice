

# exercise 2 - use formula to calculate and print table of temperatures with windspeed
def windchill(temperature, windspeed):
    if windspeed >= 3:
        windchill = 35.74 + (0.6215 * temperature) - (35.75 * (windspeed ** 0.16)) + (0.4275 * temperature) * (windspeed ** 0.16)
    else:
        windchill = 0

    return windchill


def main():

    print("{0:>}".format("Table of Windchill Values"))
    print("{0:>11} {1:6} {2:6} {3:6} {4:>6} {5:6} {6:6} {7:6} {8:6}".format(-20, -10, 0, 10, 20, 30, 40, 50, 60))
    print("")
    for i in range(11):
        print("{0:2} {1:>8.1f} {2:6.1f} {3:6.1f} {4:6.1f} {5:6.1f} {6:6.1f} {7:6.1f} {8:6.1f} {9:6.1f}"
              .format(i * 5,
                      windchill(-20, i * 5),
                      windchill(-10, i * 5),
                      windchill(0, i * 5),
                      windchill(10, i * 5),
                      windchill(20, i * 5),
                      windchill(30, i * 5),
                      windchill(40, i * 5),
                      windchill(50, i * 5),
                      windchill(60, i * 5)))


main()
# Table of Windchill Values
#         -20    -10      0     10     20     30     40     50     60
#
#  0      0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0
#  5    -34.0  -22.3  -10.5    1.2   13.0   24.7   36.5   48.2   60.0
# 10    -40.7  -28.3  -15.9   -3.5    8.9   21.2   33.6   46.0   58.4
# 15    -45.0  -32.2  -19.4   -6.6    6.2   19.0   31.8   44.6   57.5
# 20    -48.2  -35.1  -22.0   -8.9    4.2   17.4   30.5   43.6   56.7
# 25    -50.8  -37.5  -24.1  -10.7    2.6   16.0   29.4   42.8   56.1
# 30    -53.0  -39.4  -25.9  -12.3    1.3   14.9   28.5   42.0   55.6
# 35    -54.9  -41.2  -27.4  -13.6    0.1   13.9   27.7   41.4   55.2
# 40    -56.6  -42.7  -28.8  -14.8   -0.9   13.0   26.9   40.9   54.8
# 45    -58.1  -44.1  -30.0  -15.9   -1.8   12.2   26.3   40.4   54.5
# 50    -59.5  -45.3  -31.1  -16.9   -2.7   11.5   25.7   39.9   54.1