import sys
operator_fixed = ['-', '/', '*', '+']

A_number = ord('A')
N = int(sys.stdin.readline().strip())
arr = sys.stdin.readline().strip()
drr = ['' for _ in range(len(arr))]
alpha = [0 for _ in range(N)]

for i in range(N):
    alpha[i] = int(sys.stdin.readline().strip())

for i in range(len(arr)):
    if arr[i] not in operator_fixed:
        drr[i] = str(alpha[ord(arr[i]) - A_number])
    else:
        drr[i] = arr[i]

stack = list()
for i in range(len(drr)):
    if drr[i] in operator_fixed:
        b = stack.pop()
        a = stack.pop()
        if drr[i] == '+':
            ret = a + b
        elif drr[i] == '*':
            ret = a * b
        elif drr[i] == '/':
            ret = a / b
        elif drr[i] == '-':
            ret = a - b
        stack.append(ret)
    else:
        stack.append(float(drr[i]))

print(format(stack[0], ".2f"))
