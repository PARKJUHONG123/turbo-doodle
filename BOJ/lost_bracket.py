import sys

input_list = sys.stdin.readline().strip()

answer = 0
if '-' in input_list:
    minus = input_list.split('-')
    first = True
    for value in minus:
        if '+' in value:
            plus = list(map(int, value.split('+')))
            total = 0
            for element in plus:
                total += element

            if first:
                answer += total
                first = False
            else:
                answer -= total
        else:
            if len(value) == 0:
                first = False
            else:
                if first:
                    answer += int(value)
                    first = False
                else:
                    answer -= int(value)
else:
    if '+' in input_list:
        plus = list(map(int, input_list.split('+')))
        for value in plus:
            answer += value
    else:
        answer = int(input_list)

print(answer)