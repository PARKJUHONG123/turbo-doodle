N = int(input())
input_arr = [0, 0, 0]

temp_max_arr = [0, 0, 0]
temp_min_arr = [0, 0, 0]

max_arr = [0, 0, 0]
min_arr = [0, 0, 0]

for i in range(N):
    temp = input()
    temp = temp.split()
    for j in range(3):
        input_arr[j] = int(temp[j])

    if i == 0 :
        max_arr = [input_arr[0], input_arr[1], input_arr[2]]
        min_arr = [input_arr[0], input_arr[1], input_arr[2]]
        temp_max_arr = [input_arr[0], input_arr[1], input_arr[2]]
        temp_min_arr = [input_arr[0], input_arr[1], input_arr[2]]
        continue

    for j in range(3):
        if j == 0 :
            min_arr[j] = min(temp_min_arr[j], temp_min_arr[j + 1]) + input_arr[j]
            max_arr[j] = max(temp_max_arr[j], temp_max_arr[j + 1]) + input_arr[j]
        elif j == 1:
            min_arr[j] = min(temp_min_arr[j], temp_min_arr[j + 1], temp_min_arr[j - 1]) + input_arr[j]
            max_arr[j] = max(temp_max_arr[j], temp_max_arr[j + 1], temp_max_arr[j - 1]) + input_arr[j]
        else :
            min_arr[j] = min(temp_min_arr[j], temp_min_arr[j - 1]) + input_arr[j]
            max_arr[j] = max(temp_max_arr[j], temp_max_arr[j - 1]) + input_arr[j]

    temp_max_arr = max_arr[:]
    temp_min_arr = min_arr[:]
print(max(max_arr), min(min_arr))