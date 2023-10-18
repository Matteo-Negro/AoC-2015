import itertools


def read_file(filename):
    input = list()
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            tmp = line.strip().replace(',', '').split(' ')
            input.append([int(tmp[2]), int(tmp[4]), int(tmp[6]), int(tmp[8]), int(tmp[10])])
    return input


def day15_1(input, teaspoons):
    max = 0
    for comb in itertools.permutations(range(0, teaspoons + 1), len(input)):
        ts = 0
        for i in comb:
            ts += i
        if ts == teaspoons:
            sum = [0, 0, 0, 0]
            for i in range(len(input)):
                sum[0] += (input[i][0] * comb[i])
                sum[1] += (input[i][1] * comb[i])
                sum[2] += (input[i][2] * comb[i])
                sum[3] += (input[i][3] * comb[i])

            sum = [i if i >= 0 else 0 for i in sum]
            prod = 1
            for i in sum:
                prod *= i
            if prod > max:
                max = prod

    print(f'DAY15_1 results: {max}')


def day15_2(input, teaspoons, calories):
    max = 0
    for comb in itertools.permutations(range(0, teaspoons + 1), len(input)):
        ts = 0
        for i in comb:
            ts += i
        if ts == teaspoons:
            sum = [0, 0, 0, 0, 0]
            for i in range(len(input)):
                sum[0] += (input[i][0] * comb[i])
                sum[1] += (input[i][1] * comb[i])
                sum[2] += (input[i][2] * comb[i])
                sum[3] += (input[i][3] * comb[i])
                sum[4] += (input[i][4] * comb[i])

            if sum[4] != calories:
                continue

            sum = [sum[i] if sum[i] >= 0 else 0 for i in range(4)]
            prod = 1
            for i in range(4):
                prod *= sum[i]
            if prod > max:
                max = prod

    print(f'DAY15_2 results: {max}')


input = read_file('input.txt')
day15_1(input, 100)
day15_2(input, 100, 500)
