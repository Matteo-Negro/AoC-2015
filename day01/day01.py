file = open("input.txt", "r")

input = file.readline()
result = 0

for index, char in enumerate(input):
    if char == '(':
        result += 1
    else:
        result -= 1

    #Comment to run first part
    if result == -1:
        print('DAY01_2 result:', index+1)
        break

#Take off the comment below to print the first result
#print('DAY01_1 result: ', result)

file.close()
