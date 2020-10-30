import sys

stick = sys.stdin.readline().strip()
stick_start = []
answer = 0

for i in range(len(stick) - 1):
    if stick[i] == '(':
        if stick[i + 1] == '(':
            stick_start.append(i)
        else:
            answer += len(stick_start)
    else:
        if stick[i + 1] == ')':
            answer += 1
            stick_start.pop()
print(answer)