import sys
operator_dict = {
    "*" : 3,
    "/" : 3,
    "+" : 2,
    "-" : 2,
    "(" : 1,
    ")" : 0
}

arr = sys.stdin.readline().strip()
stack = list()
answer = ""
for i in range(len(arr)):
    if arr[i] in operator_dict:
        if stack:
            if arr[i] == '(':
                stack.append(arr[i])
            elif arr[i] == ')':
                while stack[-1] != '(':
                    answer += stack.pop()
                stack.pop()
            elif operator_dict[arr[i]] <= operator_dict[stack[-1]]:
                answer += stack.pop()
                stack.append(arr[i])
            else:
                stack.append(arr[i])
        else:
            stack.append(arr[i])
    else:
        answer += arr[i]

while stack:
    answer += stack.pop()
print(answer)
