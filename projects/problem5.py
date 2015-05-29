import math


def primel(n):
    primel = []
    for x in range(2, n+1):
        prime = True
        for y in range(2, int(math.sqrt(x))+1):
            if x % y == 0:
                prime = False
        if prime is True:
            primel.append(x)
    return primel

print(primel(20))


def smultiple(n):
    primeli = primel(n)
    total = 1
    for x in primeli:
        power = int((math.log(n) / math.log(x)))
        total *= pow(x, power)
    return total


print(smultiple(30))
