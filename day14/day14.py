GLOBAL_TIME = 2503
import numpy as np


def execute_1(lines):
    archive = []

    for line in lines:
        v = int(line.split(' ')[3])
        workTime = int(line.split(' ')[6])
        restTime = int(line.split(' ')[13])

        times = GLOBAL_TIME / (workTime + restTime)
        advance = round((times % 1) * (workTime + restTime))
        distance = 0
        if advance >= workTime:
            times += 1
        else:
            distance = advance * v
        distance += ((times // 1) * v * workTime)
        archive.append(distance)

        archive.sort(reverse=True)
    print('DAY14_1 result: ', archive.pop(0))


def execute_2(lines):
    archive = np.zeros(len(lines))

    for sec in range(1, GLOBAL_TIME + 1):
        winnerDist = 0
        winnerLine = []
        for index, line in enumerate(lines):
            v = int(line.split(' ')[3])
            workTime = int(line.split(' ')[6])
            restTime = int(line.split(' ')[13])

            times = sec / (workTime + restTime)
            advance = round((times % 1) * (workTime + restTime))
            distance = 0
            if advance >= workTime:
                times += 1
            else:
                distance = advance * v
            distance += ((times // 1) * v * workTime)

            if distance > winnerDist:
                winnerLine.clear()
                winnerLine.append(index)
                winnerDist = distance
            elif distance == winnerDist:
                winnerLine.append(index)
        for winner in winnerLine:
            archive[winner] += 1
    print('DAY14_2 result: ', archive.max())


with open('input.txt') as file:
    input = file.readlines()

    execute_1(input)
    execute_2(input)
