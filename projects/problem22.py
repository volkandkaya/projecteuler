def score(name, n):
    uname = name.upper()
    score = 0
    for x in range(1, len(uname)-1):
        score += ord(uname[x]) - 64
    return score * n

with open('names.txt', 'r') as f:
    data = f.readlines()
    for word in data:
        words = word.split(',')

sortedwords = sorted(words)

total = 0
for y in range(0, len(sortedwords)):
    total += score(sortedwords[y], y + 1)

print(total)
