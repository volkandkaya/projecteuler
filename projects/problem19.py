def leap(year):
    leap = 28
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = 29
            else:
                leap = 28
        else:
            leap = 29
    return leap

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
total = 0
year = 1900
day = 1

for x in days:
    if x == 28:
        day += leap(year)
    else:
        day += x

day = day % 7

for x in range(1901, 2001):
    for y in days:
        if y == 28:
            day += leap(year)
            if day % 7 == 0:
                total += 1
        else:
            day += y
            if day % 7 == 0:
                total += 1
print(total)
