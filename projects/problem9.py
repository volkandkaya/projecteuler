def ab(a, b):
    return 2000*a + 2000*b - 2*a*b


def pytriplet(n):
    a = 0
    b = 0
    c = 0
    for x in range(1, int(n/2)):
        for y in range(1, x):
            if ab(x, y) == n**2:
                b = x
                a = y
    c = n - a - b
    print(a, b, c)

pytriplet(1000)
