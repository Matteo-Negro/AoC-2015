import numpy as np


def minPath(minMatrix, lenLocations):
    passages = np.zeros(lenLocations)
    minMatrix = np.where(minMatrix > 0, minMatrix, np.inf)

    result = 0
    while True:
        if passages.sum() == (2 * lenLocations) - 2:
            break

        minValue = np.amin(minMatrix)
        indexMinValue = np.argmin(minMatrix)
        minMatrix[indexMinValue // lenLocations][indexMinValue % lenLocations] = np.inf

        if passages[indexMinValue // lenLocations] >= 2 or passages[indexMinValue % lenLocations] >= 2:
            continue
        if passages[indexMinValue // lenLocations] < 2:
            passages[indexMinValue // lenLocations] += 1
        if passages[indexMinValue % lenLocations] < 2:
            passages[indexMinValue % lenLocations] += 1
        result += minValue

    return result


def maxPath(maxMatrix, lenLocations):
    passages = np.zeros(lenLocations)
    maxMatrix = np.where(maxMatrix > 0, maxMatrix, -np.inf)

    result = 0
    while True:
        if passages.sum() == (2 * lenLocations) - 2:
            break

        maxValue = np.amax(maxMatrix)
        indexMaxValue = np.argmax(maxMatrix)
        maxMatrix[indexMaxValue // lenLocations][indexMaxValue % lenLocations] = -np.inf

        if passages[indexMaxValue // lenLocations] >= 2 or passages[indexMaxValue % lenLocations] >= 2:
            continue
        if passages[indexMaxValue // lenLocations] < 2:
            passages[indexMaxValue // lenLocations] += 1
        if passages[indexMaxValue % lenLocations] < 2:
            passages[indexMaxValue % lenLocations] += 1
        result += maxValue

    return result


with open('input.txt') as file:
    lines = file.readlines()
    locations = []

    for line in lines:
        tmp1 = line.split(' ')

        if tmp1[0] not in locations:
            locations.append(tmp1[0])
        if tmp1[2] not in locations:
            locations.append(tmp1[2])

    matrix = np.zeros((len(locations), len(locations)))

    for line in lines:
        tmp1 = line.split(' ')
        matrix[locations.index(tmp1[0])][locations.index(tmp1[2])] = tmp1[4]

    print('DAY09_1 result: ', minPath(matrix, len(locations)))
    print('DAY09_2 result: ', maxPath(matrix, len(locations)))
