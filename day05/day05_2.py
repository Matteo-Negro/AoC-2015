import re

file = open("input.txt", "r")

lines = file.readlines()
result = 0

for line in lines:
    temp = False
    # First rule
    for index, char in enumerate(line):
        if index + 1 < len(line) and len(re.findall(line[index:(index + 2)], line)) == 2:
            temp = True

    # Second rule
    if not temp:
        continue

    for index, char in enumerate(line):
        if index + 2 < len(line) and line[index + 2] == char:
            result += 1
            break

print('DAY05_02 result: ', result)

file.close()
