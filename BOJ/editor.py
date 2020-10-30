import sys
stack_a = list(map(str, sys.stdin.readline().strip()))
stack_b = list()

N = int(sys.stdin.readline().strip())

for _ in range(N):
    com = sys.stdin.readline().split()

    if len(com) == 2:
        stack_a.append(com[1])

    else:
        if com[0] == 'L':
            if stack_a:
                stack_b.append(stack_a.pop())
        elif com[0] == 'D':
            if stack_b:
                stack_a.append(stack_b.pop())
        elif com[0] == 'B':
            if stack_a:
                stack_a.pop()

answer = ""
for value in stack_a:
    answer += value
for value in reversed(stack_b):
    answer += value
print(answer)