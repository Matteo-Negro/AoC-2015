import copy

def read_input(filename='input.txt'):
    input = dict()
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            pieces = line.strip()[:-1].split(' ')
            factor = 1 if pieces[2] == 'gain' else -1
            if pieces[0] not in input.keys():
                input[pieces[0]] = dict()
            input[pieces[0]][pieces[-1]] = factor * int(pieces[3])

    return input


def build_tree(input, superroot, root, trace,  finalstep, results, currstep=0, score=0):
    if currstep == finalstep:
        for branch in input[root].keys():
            if branch == superroot:
                results.append(score + input[root][branch] + input[branch][root])
        return
    for branch in input[root].keys():
        if branch not in trace:
            tmp = copy.deepcopy(trace)
            tmp.add(branch)
            build_tree(input, superroot, branch, tmp, finalstep, results, currstep + 1, score + input[root][branch] + input[branch][root])


input_1 = read_input('input.txt')
keys = list(input_1.keys())

results_1 = list()
build_tree(input_1, keys[0], keys[0], {keys[0]},  len(keys) - 1, results_1)
print(f'DAY13_1 result: {max(results_1)}')

input_2 = copy.deepcopy(input_1)
input_2['Teo'] = dict()
for k in keys:
    input_2['Teo'][k] = 0
    input_2[k]['Teo'] = 0
keys = list(input_2.keys())

results_2 = list()
build_tree(input_2, keys[0], keys[0], {keys[0]}, len(keys) - 1, results_2)
print(f'DAY13_2 result: {max(results_2)}')

