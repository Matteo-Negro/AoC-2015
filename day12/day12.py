import re

with open('input.txt') as file:
    input = file.readline()

    input = re.sub(':|"|[a-z]|\{|\}|\[|\]', '', input).split(',')

    result = 0
    for elem in input:
        if elem.strip() != '':
            result += int(elem.strip())
    print('DAY12_1 result: ', result)
