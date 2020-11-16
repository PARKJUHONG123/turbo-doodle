import sys
input_num = sys.stdin.readline().strip()
delete_num = sys.stdin.readline().strip()
count = [0 for _ in range(10)]

for i in range(len(delete_num)):
    count[int(delete_num[i])] += 1

num_index = [0 for _ in range(len(input_num))]
number_count = [0 for _ in range(10)]

for i in reversed(range(len(input_num))):
    number = int(input_num[i])
    number_count[number] += 1
    num_index[i] = number_count[number]

def make_pair(x):
    count_temp = [0 for _ in range(10)]
    for i in range(10):
        count_temp[i] = count[i]

    ret = [x, int(input_num[x])]
    while True:
        number = int(input_num[x])
        if not count_temp[number]:
            break
        if number > ret[1] and count_temp[number] < num_index[x]:
            ret = [x, number]
        count_temp[number] -= 1
        x += 1

    number = int(input_num[x])
    if number > ret[1] and count_temp[number] < num_index[x]:
        ret = [x, number]
    return ret

index, answer = 0, ''
while index < len(input_num):
    number = int(input_num[index])
    if count[number] == 0:
        answer += (input_num[index])
        index += 1

    elif count[number] == num_index[index]:
        count[number] -= 1
        index += 1

    else:
        pair = make_pair(index)
        for i in range(index, pair[0]):
            count[int(input_num[i])] -= 1
        index = pair[0] + 1
        answer += str(pair[1])
print(answer)
