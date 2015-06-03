import math

x = 0
nom = 0
z = 0
while(nom < 500):
    x += 1
    nom = 0
    z += x
    for y in range(1, int(math.sqrt(z)) + 1):
        if z % y == 0:
            nom += 2

print(z)
