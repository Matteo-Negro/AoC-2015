RELACEMETS = []
COMBINATIONS = {}

with open('input.txt') as file:
    lines = file.readlines()

    for index, line in enumerate(lines):
        line = line.strip()
        if index == len(lines) - 1:
            MOLECULE = line.strip()
        elif line != '':
            RELACEMETS.append(line.strip())

for elem in RELACEMETS:
    rule = elem.split(' => ')
    dim = len(rule[0])

    for index, char in enumerate(MOLECULE):
        if MOLECULE[index:index + dim] == rule[0]:
            tmp = ''
            tmp += MOLECULE[:index]
            tmp += rule[1]
            tmp += MOLECULE[index+dim:]
            COMBINATIONS[tmp] = ''

print('DAY19_1 result: ', len(COMBINATIONS))
