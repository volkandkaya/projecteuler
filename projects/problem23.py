from math import sqrt


def sumof(n):
    sum = 1
    t = sqrt(n)
    # only proper divisors; start from 2.
    for i in range(2, int(t)+1):
        if n % i == 0:
            sum += i + n / i
    # don't count the square root twice!
    if t == int(t):
        sum -= t
    return sum

limit = 28124
sum = 0

abn = set()
for n in range(1, limit):
    if sumof(n) > n:
        abn.add(n)
    if not any((n-a in abn) for a in abn):
        sum += n

print(sum)

