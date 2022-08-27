def increase(workingStr):
    if len(workingStr) == 1 and workingStr == 'z':
        return 'aa'
    elif ord(workingStr[len(workingStr) - 1]) < ord('z'):
        tmp = workingStr[len(workingStr) - 1]
        workingStr = workingStr[:-1]
        workingStr += chr(ord(tmp) + 1)
        return workingStr
    else:
        workingStr = increase(workingStr[:-1])
        workingStr += 'a'
        return workingStr


input = 'vzbxkghb'

while True:
    input = increase(input)

    # First requirement
    first = False
    charPrev = ''
    for char in input:
        if charPrev == '' or ord(charPrev) != ord(char) - 1:
            sequence = 1
        else:
            sequence += 1
            if sequence == 3:
                first = True
                break
        charPrev = char
    if not first:
        continue

    # Second requirement
    second = True
    for char in input:
        if char == 'i' or char == 'o' or char == 'l':
            second = False
            break
    if not second:
        continue

    # Third requirement
    third1 = False
    third2 = False
    charPrev = ''
    for char in input:
        if charPrev == '' or charPrev != char:
            charPrev = char
        elif not third1:
            third1 = True
            charPrev = ''
        else:
            third2 = True
            break
    if third2:
        print('DAY11_1 result: ', input)
        break
