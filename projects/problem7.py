import math


def prime_check(n):
    if n < 2:
        return False
    for x in range(2, int(math.sqrt(n))+1):
        if n % x == 0:
            return False
    return True


def pn(n):
    no = 0
    prime = 0
    x = 1
    while (no < n):
        primecheck = prime_check(x)
        if primecheck is True:
            no += 1
            prime = x
        x += 1
    return prime

print(pn(10001))
