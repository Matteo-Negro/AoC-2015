file = open("input.txt", "r")

lines = file.readlines()
result1 = 0
result2 = 0

for line in lines:
    dim = [int(i, base=10) for i in line.split('x')]
    dim.sort()

    result1 += (3 * dim[0] * dim[1] + 2 * dim[0] * dim[2] + 2 * dim[1] * dim[2])
    result2 += (2*dim[0] + 2*dim[1] + dim[0]*dim[1]*dim[2])

print('DAY02_01 result: ', result1)
print('DAY02_02 result: ', result2)

file.close()