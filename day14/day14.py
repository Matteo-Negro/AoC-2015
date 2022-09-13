GLOBAL_TIME = 2503

with open('input.txt') as file:
    lines = file.readlines()
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
