import re


def execute_1(data):
    data = re.sub(':|"|[a-z]|\{|\}|\[|\]', '', data).split(',')

    result = 0
    for elem in data:
        if elem.strip() != '':
            result += int(elem.strip())
    print('DAY12_1 result: ', result)


def execute_2(data):
    data = re.sub(':|,', '#', data)
    data = re.sub('\[', '[#', data)
    data = re.sub('\{', '{#', data)
    data = re.sub('\]', '#]', data)
    data = re.sub('\}', '#}', data)
    data = data.split('#')

    tmp = 0
    values = []
    bracket = []
    for elem in data:
        elem = elem.strip()

        if elem == '}':
            if tmp != '#' and values[len(values) - 1] != '#':
                tmp += values[len(values) - 1]
            elif bracket.count('{') == 2 and tmp != '#':
                continue
            else:
                tmp = values[len(values) - 1]
            bracket.pop()
            values.pop()
        elif elem == '{':
            values.append(tmp)
            if tmp != '#' or bracket.count('{') == 1:
                tmp = 0
            bracket.append('{')
        elif elem == ']':
            bracket.pop()
        elif elem == '[':
            bracket.append('[')
        elif elem == '"red"' and bracket[len(bracket) - 1] == '{':
            tmp = '#'
        elif elem.replace('-', '').isdigit() and tmp != '#':
            tmp += int(elem)

    print('DAY12_2 result: ', 0 if tmp == '#' else tmp)


with open('input.txt') as file:
    input = file.readline()

    execute_1(input)
    execute_2(input)
