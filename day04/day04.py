import hashlib

input = 'bgvyzdsv'
result = 0

while True:
    hash = hashlib.md5((input + str(result)).encode())
    # if str(hash.hexdigest())[0:5] == '00000':
        # print(hash.hexdigest())
        # print('DAY04_1 result: ', result)
        # break
    if str(hash.hexdigest())[0:6] == '000000':
        print(hash.hexdigest())
        print('DAY04_2 result: ', result)
        break
    result += 1
