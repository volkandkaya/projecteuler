def route_num(size):
    l = [1] * size
    for i in range(size):
        for j in range(i):
            l[j] = l[j]+l[j-1]
        l[i] = 2 * l[i - 1]
    return l[size - 1]

print(route_num(3))
