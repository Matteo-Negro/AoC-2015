import copy

RELACEMETS_1 = []
RELACEMETS_2 = {}


def day19_1(RELACEMETS, MOLECULE):
    COMBINATIONS = {}

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

def day19_2(RELACEMETS, MOLECULE, root = 'e'):
    result = 1
    # BFS
    seen = set()
    queue = [elem for elem in RELACEMETS[root]]
    queue.append('#')
    while queue:
        val = queue.pop(0)
        if val == '#':
            result += 1
            val = queue.pop(0)
            queue.append('#')

            print(f'Update shortest: {result}')
        forks = fork_dict(RELACEMETS.keys(), val)
        for branch in forks.keys():
            for index in forks[branch]:
                for rule in RELACEMETS[branch]:
                    tmp = ''
                    tmp += val[:index]
                    tmp += rule
                    tmp += val[(index + len(branch)):]
                    if tmp not in seen:
                        seen.add(tmp)
                        queue.append(tmp)
                    
                    if tmp == MOLECULE:
                        print('DAY19_2 result: ', result + 1)
                        return
    







def fork_dict(rules, root):
    forks = dict()
    for i in range(len(root)):
        if root[i] in rules:
            if root[i] not in forks.keys():
                forks[root[i]] = list()
            forks[root[i]].append(i)
        if i < len(root) - 1 and root[i:i+2] in rules:
            if root[i:i+2] not in forks.keys():
                forks[root[i:i+2]] = list()
            forks[root[i:i+2]].append(i)
    return forks


with open('/Users/matteoblack/Desktop/Proj/AoC-2015/day19/input.txt') as file:
    lines = file.readlines()

    for index, line in enumerate(lines):
        line = line.strip()
        if index == len(lines) - 1:
            MOLECULE = line.strip()
        elif line != '':
            RELACEMETS_1.append(line.strip())

            tmp = line.strip().split(' => ')
            if tmp[0] not in RELACEMETS_2.keys():
                RELACEMETS_2[tmp[0]] = list()

            RELACEMETS_2[tmp[0]].append(tmp[1])

day19_1(RELACEMETS_1, MOLECULE)
day19_2(RELACEMETS_2, MOLECULE)