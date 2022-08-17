import re

file = open('input.txt', 'r')
workFile = open('workFile.txt', 'r+')
lines = file.readlines()
wires = {}

while True:
    print(len(lines))
    workFile.seek(0)
    workFile.truncate()
    for line in lines:
        cmd = line.split(' -> ')
        cmd_input = cmd[0].split(' ')
        cmd[1] = cmd[1].replace('\n', '')

        if len(cmd_input) == 1:
            if (cmd_input[0].isdigit()) or cmd_input[0] in wires.keys():
                wires[cmd[1]] = int(cmd_input[0]) if cmd_input[0].isdigit() else wires[cmd_input[0]]
            else:
                workFile.write(line)
                workFile.flush()

        elif len(cmd_input) == 2:
            if (cmd_input[1].isdigit()) or cmd_input[1] in wires.keys():
                wires[cmd[1]] = ~int(cmd_input[1]) if cmd_input[0].isdigit() else ~int(wires[cmd_input[1]])
            else:
                workFile.write(line)
                workFile.flush()

        elif len(cmd_input) == 3:
            if re.search('RSHIFT', cmd[0]):
                if cmd_input[0] in wires.keys():
                    wires[cmd[1]] = int(wires[cmd_input[0]]) >> int(cmd_input[2])
                else:
                    workFile.write(line)
                    workFile.flush()
            elif re.search('LSHIFT', cmd[0]):
                if cmd_input[0] in wires.keys():
                    wires[cmd[1]] = int(wires[cmd_input[0]]) << int(cmd_input[2])
                else:
                    workFile.write(line)
                    workFile.flush()
            elif re.search('AND', cmd[0]):
                if (cmd_input[0].isdigit() or cmd_input[0] in wires.keys()) and (
                        cmd_input[2].isdigit() or cmd_input[2] in wires.keys()):
                    wires[cmd[1]] = (int(cmd_input[0]) if cmd_input[0].isdigit() else int(wires[cmd_input[0]])) & (
                        int(cmd_input[2]) if cmd_input[2].isdigit() else int(wires[cmd_input[2]]))
                else:
                    workFile.write(line)
                    workFile.flush()
            elif re.search('OR', cmd[0]):
                if (cmd_input[0].isdigit() or cmd_input[0] in wires.keys()) and (
                        cmd_input[2].isdigit() or cmd_input[2] in wires.keys()):
                    wires[cmd[1]] = (int(cmd_input[0]) if cmd_input[0].isdigit() else int(wires[cmd_input[0]])) | (
                        int(cmd_input[2]) if cmd_input[2].isdigit() else int(wires[cmd_input[2]]))
                else:
                    workFile.write(line)
                    workFile.flush()

    workFile.seek(0)
    lines = workFile.readlines()
    if len(lines) == 0:
        break

# To print the result of the second task override line 335 with the value obtain with the first input
print('DAY07 result: \n', wires['a'])
file.close()
workFile.close()
