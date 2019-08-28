from random import random
print(random())
print(random())
print(random())
print(random())
print(random())
print(random())
# simulation 1
# 0.7379727426848471
# 0.018733313134947527
# 0.10286965161146011
# 0.5599289504048554
# 0.48559188569939093
# 0.7217762924986684

# simulation 2
# 0.9382101213047461
# 0.41265771962466635
# 0.22939408400045613
# 0.26125647691878506
# 0.7457415294890736
# 0.07449767785377859


def proability():
    prob = .7
    score = 1
    for i in range(10):
        if random() < prob:
            score = score + 1
    print(score)


proability()
# simulation 1 = 10
# simulation 2 = 8
# simulation 3 = 6
