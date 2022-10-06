import sympy as sy

input = 34000000

result = 0
times = 1

while result < input:
    times += 1
    div = list(sy.divisors(times, generator=True))
    div.sort(reverse=True)

    if len(div) == 2:
        continue

    result = 0
    for index in range(min(len(div), 50)):
        if times // div[index] > 50:
            break
        result += (div[index]*11)

print('DAY20_2 result: ', times, '-', result)
