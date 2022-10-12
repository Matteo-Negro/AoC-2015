# a = 0 for part 1
# a = 1 for part 2
a = 1
b = 0

with open('input.txt') as file:
    lines = file.readlines()

index = 0
while True:
    if len(lines) <= index:
        break

    line = lines[index].strip().replace(',', '')
    line = line.split(' ')

    if line[0] == 'hlf':
        if line[1] == 'a':
            a //= 2
        else:
            b //= 2
    elif line[0] == 'tpl':
        if line[1] == 'a':
            a *= 3
        else:
            b *= 3
    elif line[0] == 'inc':
        if line[1] == 'a':
            a += 1
        else:
            b += 1
    elif line[0] == 'jmp':
        offset = int(line[1])
        index += offset
        continue
    elif line[0] == 'jie':
        offset = int(line[2])
        if line[1] == 'a' and a % 2 == 0:
            index += offset
            continue
        elif line[1] == 'b' and b % 2 == 0:
            index += offset
            continue
    elif line[0] == 'jio':
        offset = int(line[2])
        if line[1] == 'a' and a == 1:
            index += offset
            continue
        elif line[1] == 'b' and b == 1:
            index += offset
            continue
    index += 1

print(f'DAY23 result: {b}')
