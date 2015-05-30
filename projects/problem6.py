def sumsquaredifference(n):
    sums = 0
    squares = 0
    for x in range(1, n+1):
        sums += x**2
        squares += x
    return squares**2 - sums

print(sumsquaredifference(100))
