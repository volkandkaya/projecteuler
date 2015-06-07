def pow(exp):
    pow = list(str(2**exp))
    return sum([int(i) for i in pow])

print(pow(1000))
