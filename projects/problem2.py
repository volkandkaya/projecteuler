total = 0
xold1 = 1
xold2 = 1
xnew = 2
while xnew < 4000000:
    if xnew % 2 == 0:
        total += xnew
        xold2 = xold1
        xold1 = xnew
        xnew += xold2
        print(xnew)
    else:
        xold2 = xold1
        xold1 = xnew
        xnew += xold2
        print(xnew)

print(total)
