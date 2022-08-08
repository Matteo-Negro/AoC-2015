import re

file = open("input.txt", "r")

lines = file.readlines()
result = 0

for line in lines:
    # Third rule
    if re.search('ab|cd|pq|xy', line):
        continue

    # First rule
    vowels = 0
    for char in line:
        if re.search('a|e|i|o|u', char):
            vowels += 1
        if vowels == 3:
            # Second rule
            for index, char in enumerate(line):
                if index + 1 < len(line) and line[index + 1] == char:
                    result += 1
                    break
            break

print('DAY05_01 result: ', result)

file.close()
