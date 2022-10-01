TIMES = 100
matrixA = []
matrixB = []


def copyMatrix(matIn, matOut):
    for r in range(len(matIn)):
        matOut[r] = matIn[r].copy()
    return matOut


def helperPart2(matrix1):
    matrix1[0][0] = '#'
    matrix1[0][len(matrix1[0]) - 1] = '#'
    matrix1[len(matrix1) - 1][len(matrix1[0]) - 1] = '#'
    matrix1[len(matrix1) - 1][0] = '#'
    return matrix1


def execute(matrix1, matrix2, part2=False):
    if part2:
        helperPart2(matrix1)

    for _ in range(TIMES):
        for row in range(len(matrix1)):
            for col in range(len(matrix1[0])):
                counter = 0
                if row != 0 and col != 0 and matrix1[row - 1][col - 1] == '#':
                    counter += 1
                if row != 0 and matrix1[row - 1][col] == '#':
                    counter += 1
                if row != 0 and col != len(matrix1[0]) - 1 and matrix1[row - 1][col + 1] == '#':
                    counter += 1
                if col != len(matrix1[0]) - 1 and matrix1[row][col + 1] == '#':
                    counter += 1
                if row != len(matrix1) - 1 and col != len(matrix1[row]) - 1 and matrix1[row + 1][col + 1] == '#':
                    counter += 1
                if row != len(matrix1) - 1 and matrix1[row + 1][col] == '#':
                    counter += 1
                if row != len(matrix1) - 1 and col != 0 and matrix1[row + 1][col - 1] == '#':
                    counter += 1
                if col != 0 and matrix1[row][col - 1] == '#':
                    counter += 1

                if matrix1[row][col] == '#' and counter != 2 and counter != 3:
                    matrix2[row][col] = '.'
                elif matrix1[row][col] == '.' and counter == 3:
                    matrix2[row][col] = '#'
        matrix1 = copyMatrix(matrix2, matrix1)

        if part2:
            helperPart2(matrix1)

    result = 0
    for i in range(len(matrixA)):
        result += matrixA[i].count('#')

    return result


with open('input.txt') as file:
    lines = file.readlines()
    for line in lines:
        rowTmp = []
        for char in line.strip():
            rowTmp.append(char)
        matrixA.append(rowTmp)
        matrixB.append(rowTmp.copy())

print('DAY18 result: ', execute(matrixA, matrixB, True))
