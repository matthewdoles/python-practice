def addInterest(balance, rate):
    newBalance = balance * (1 + rate)
    return newBalance


def test():
    amount = 1000
    rate = 0.05
    amount = addInterest(amount, rate)
    print(amount)


def addInterests(balances, rate):
    for i in range(len(balances)):
        balances[i] = balances[i] * (1 + rate)


def test2():
    amounts = [1000, 2200, 800, 360]
    rate = 0.05
    addInterests(amounts, rate)
    print(amounts)


test()
# 1050.0
test2()
# [1050.0, 2310.0, 840.0, 378.0]
