import numpy as np


def execute_1(commands):
    grid = np.zeros((1000, 1000))
    for line in commands:
        command = line.split(' ')
        if command[0] == 'toggle':
            coord_start = command[1].split(',')
            coord_end = command[3].split(',')
            for r in range(int(coord_start[0]), int(coord_end[0]) + 1):
                for c in range(int(coord_start[1]), int(coord_end[1]) + 1):
                    grid[r][c] = 1 if grid[r][c] == 0 else 0
        elif command[1] == 'on':
            coord_start = command[2].split(',')
            coord_end = command[4].split(',')
            for r in range(int(coord_start[0]), int(coord_end[0]) + 1):
                for c in range(int(coord_start[1]), int(coord_end[1]) + 1):
                    grid[r][c] = 1
        elif command[1] == 'off':
            coord_start = command[2].split(',')
            coord_end = command[4].split(',')
            for r in range(int(coord_start[0]), int(coord_end[0]) + 1):
                for c in range(int(coord_start[1]), int(coord_end[1]) + 1):
                    grid[r][c] = 0

    print('DAY06_1 result: ', grid.sum())


def execute_2(commands):
    grid = np.zeros((1000, 1000))
    for line in commands:
        command = line.split(' ')
        if command[0] == 'toggle':
            coord_start = command[1].split(',')
            coord_end = command[3].split(',')
            for r in range(int(coord_start[0]), int(coord_end[0]) + 1):
                for c in range(int(coord_start[1]), int(coord_end[1]) + 1):
                    grid[r][c] += 2
        elif command[1] == 'on':
            coord_start = command[2].split(',')
            coord_end = command[4].split(',')
            for r in range(int(coord_start[0]), int(coord_end[0]) + 1):
                for c in range(int(coord_start[1]), int(coord_end[1]) + 1):
                    grid[r][c] += 1
        elif command[1] == 'off':
            coord_start = command[2].split(',')
            coord_end = command[4].split(',')
            for r in range(int(coord_start[0]), int(coord_end[0]) + 1):
                for c in range(int(coord_start[1]), int(coord_end[1]) + 1):
                    grid[r][c] = 0 if grid[r][c] == 0 else grid[r][c] - 1

    print('DAY06_2 result: ', grid.sum())


file = open('input.txt', 'r')

lines = file.readlines()

execute_1(lines)
execute_2(lines)

file.close()
