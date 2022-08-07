file = open("input.txt", "r")

input = file.readline()
x = 0
y = 0
x_even = 0
y_even = 0
x_odd = 0
y_odd = 0
coord1 = ['0,0']
coord2 = ['0,0']

for index, char in enumerate(input):
    if char == '^':
        y += 1
        if (index + 1) % 2 == 0:
            y_even += 1
        else:
            y_odd += 1
    elif char == 'v':
        y -= 1
        if (index + 1) % 2 == 0:
            y_even -= 1
        else:
            y_odd -= 1
    elif char == '>':
        x += 1
        if (index + 1) % 2 == 0:
            x_even += 1
        else:
            x_odd += 1
    elif char == '<':
        x -= 1
        if (index + 1) % 2 == 0:
            x_even -= 1
        else:
            x_odd -= 1

    # First part
    temp = '' + str(x) + ',' + str(y)
    if temp not in coord1:
        coord1.append(temp)

    # Second part
    if (index + 1) % 2 == 0:
        temp = '' + str(x_even) + ',' + str(y_even)
    else:
        temp = '' + str(x_odd) + ',' + str(y_odd)
    if temp not in coord2:
        coord2.append(temp)

print('DAY03_1 result: ', len(coord1))
print('DAY03_2 result: ', len(coord2))

file.close()
