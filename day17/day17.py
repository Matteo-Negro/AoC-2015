LITERS = 150
result_2 = []


def day17_1(liters, containers):
    result_1 = 0
    if containers is None:
        return 0
    elif liters in containers:
        result_1 += containers.count(liters)
    for index, elem in enumerate(containers):
        if liters - elem > 0:
            result_1 += day17_1(liters - elem, containers[index + 1:])
    return result_1


def day17_2(liters, containers, deep=0):
    if liters in containers:
        deep += 1
        for _ in range(containers.count(liters)):
            result_2.append(deep)
    for index, elem in enumerate(containers):
        deepTmp = deep
        if liters - elem > 0:
            deepTmp += 1
            day17_2(liters - elem, containers[index + 1:], deepTmp)


with open('input.txt') as file:
    input = []
    lines = file.readlines()
    for line in lines:
        input.append(int(line.strip()))

    day17_2(LITERS, input)
    result_2.sort()

    print('DAY17_1 result: ', day17_1(150, input))
    print('DAY17_2 result: ', result_2.count(result_2[0]))
