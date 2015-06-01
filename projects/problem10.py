import math


def prime_check(n):
    if n < 2:
        return False
    for x in range(2, int(math.sqrt(n))+1):
        if n % x == 0:
            return False
    return True


def primesum(m):
    x = 2
    total = 0
    while(x < m):
        if prime_check(x) is True:
            total += x
            print(x)
        x += 1
    return total

print(primesum(2000000))
