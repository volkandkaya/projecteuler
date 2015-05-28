value = 0

for m in range(1000, -1, -1):
    for n in range(1000, -1, -1):
        total = m*n
        strn = str(total)
        if strn == strn[::-1]:
            if value < total:
                value = total
                print(m, n, total)
