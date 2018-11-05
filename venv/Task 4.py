import random

def sumdice(dice, numrolls):
    sum1 = 0
    for x in range(numrolls):
        sum1 = sum1 + random.randint(1,dice)
    return sum1

print(sumdice(4,3))