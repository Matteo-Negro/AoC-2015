input = '1113122113'

for _ in range(50):
    tmp = ''
    charPrev = ''
    occurrences = 0
    for char in input:
        if charPrev != '' and charPrev != char:
            tmp += str(occurrences)
            tmp += charPrev
            occurrences = 0
        occurrences += 1
        charPrev = char
    tmp += str(occurrences)
    tmp += charPrev
    input = tmp

print('DAY10 result: ', len(input))
