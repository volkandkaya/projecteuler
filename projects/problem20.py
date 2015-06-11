def fact(n):
    total = n
    if n > 1:
        total *= fact(n-1)
    return total
print(fact(100))


def factsum(n):
    total = str(fact(n))
    sumof = 0
    for x in range(0, len(total)):
        sumof += int(total[x])
    return sumof

print(factsum(100))
