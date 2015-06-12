from math import sqrt


def sumof(n):
    sqrtn = int(sqrt(n))
    if n > 1:
        total = 1
        if n == sqrtn ** 2:
            total += sqrtn
        for x in range(2, sqrtn):
            if n % x == 0:
                total += x + (n/x)
    return int(total)

sumAmicible = 0
upperlimit = 10001

for x in range(2, upperlimit):
    factorx = sumof(x)
    if (factorx > x) and (factorx < upperlimit):
        factorj = sumof(factorx)
        if factorj == x:
            sumAmicible += x + factorx
print(sumAmicible)
