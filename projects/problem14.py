def collatz(n):
    old = 1
    bigx = 1
    d = {}
    for x in range(2, n):
        oldx = x
        new = 1
        while(x > 1):
            if x % 2 == 0:
                x = x // 2
            else:
                x = 3*x+1
            new += 1
            if (x > 1) & (x < oldx):
                new += d[x] - 1
                x = 1
        d[oldx] = new
        if old < new:
            old = new
            bigx = oldx
            print(bigx, old)
    return bigx

print(collatz(100000))
