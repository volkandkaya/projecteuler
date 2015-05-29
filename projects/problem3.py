import math

n = 100
i = 2
factors = []
while i < math.sqrt(n)+1:
    print(i)
    while n % i == 0:
        n = n//i
        factors.append(i)
    i += 1
factors.append(n)
factors.remove(1)
largest = max(factors)
print(factors)
print(largest)
