with open('input.txt') as file:
    lines = file.readlines()

    strLiterals_1 = 0
    strLiterals_2 = 0
    chrMemory = 0
    for line in lines:
        line = line.replace('\n', '')
        char = 1
        strLiterals_1 += len(line)
        strLiterals_2 += (len(line) + 4)
        while line[char] != '"':
            if line[char] != '\\':
                chrMemory += 1
            elif line[char + 1] == 'x':
                strLiterals_2 += 1
                chrMemory += 1
                char += 3
            else:
                strLiterals_2 += 2
                chrMemory += 1
                char += 1
            char += 1

    result_1 = strLiterals_1 - chrMemory
    result_2 = strLiterals_2 - strLiterals_1

    print('DAY08_1 result: ', result_1)
    print('DAY08_2 result: ', result_2)
