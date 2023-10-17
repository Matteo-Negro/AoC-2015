import numpy as np
import math

row = 2947
col = 3029

mult  = 252533
div   = 33554393
start = 20151125

index = int((((row + col - 2) * (row + col -1))/(2)) + col - 1)

result = start
for i in range(index):
    result *= mult
    result %= div

print(f'DAY25 result: {result}')

# print(f'index: {index}')
# up = int(math.pow(mult, index))
# result = (start * int(up)) % div
# print(result)