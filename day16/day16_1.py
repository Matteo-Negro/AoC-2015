import re

tickerTape = {}

with open('tickerTape.txt') as tickerFile:
    lines = tickerFile.readlines()
    for line in lines:
        input = line.strip().split(': ')
        tickerTape[input[0]] = input[1]

with open('input.txt') as inputFile:
    lines = inputFile.readlines()
    for line in lines:
        find = 0
        line = re.sub(':|,', '', line)
        input = line.strip().split(' ')
        for index, elm in enumerate(input):
            if index < 2 or index % 2 != 0:
                continue
            if elm in tickerTape and tickerTape[elm] == input[index + 1]:
                find += 1
        if find == (len(input) - 2) / 2:
            print('DAY16_1 result: ', input[1])
            break
