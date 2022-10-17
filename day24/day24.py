import numpy as np


def findCombination(weightFree, pos, res, dep=[], first=True, counter=0, limiter=np.inf):
    counter += 1
    if counter > limiter or len(pos) == 0 or weightFree - pos[0] < 0:
        dep.append('#')
        res.append(dep)
        return limiter
    if weightFree in pos:
        dep.append(weightFree)
        res.append(dep)
        return len(dep)

    for i, g in enumerate(pos):

        depTmp = dep.copy()
        depTmp.append(g)
        limiter = findCombination(weightFree - g, pos[i + 1:], res, depTmp, False, counter, limiter)
    return limiter


input = []
with open('input.txt') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        input.append(int(line))

sum = 0
for w in input:
    sum += w

result = []
# To compute PART1 -> sum // 3
# To compute PART2 -> sum // 4
findCombination(sum // 4, input, result)

minLen = np.inf
for el in result:
    if '#' not in el:
        if minLen > len(el):
            minQE = 1
            for w in el:
                minQE *= w
            minLen = len(el)
        elif minLen == len(el):
            tmpQE = 1
            for w in el:
                tmpQE *= w
            if minQE > tmpQE:
                minQE = tmpQE

print(f'DAY24 result: {minQE}')
