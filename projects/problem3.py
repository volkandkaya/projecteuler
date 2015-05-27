import math

n = 600851475143
i = 2
factors = []
while i < math.sqrt(n):
    while n % i == 0:
        n = n/i
        factors.append(i)
    i += 1
factors.append(n)
largest = max(factors)
print(factors)
print(largest)
