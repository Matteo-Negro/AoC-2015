import sympy as sy
import numpy as np
import math as mt

input = 34000000 / 10

result = 0
times = 1

while result < input:
    times += 1
    primeFactors = sy.primefactors(times)
    occ = np.zeros(len(primeFactors), dtype=int)

    i = 0
    num = times
    while True:
        if num == 1:
            break
        if num % primeFactors[i] == 0:
            occ[i] += 1
            num /= primeFactors[i]
        else:
            i += 1

    result = 1
    for index, pf in enumerate(primeFactors):
        result *= (((mt.pow(pf, (occ[index] + 1))) - 1) / (pf - 1))
    result += 1

print('DAY20_1 result: ', times)
