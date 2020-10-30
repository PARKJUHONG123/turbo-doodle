import sys

N = int(sys.stdin.readline().strip())

will_add_number = 1
stack = list()
answer = list()

for _ in range(N):
    M = int(sys.stdin.readline().strip())
    if M > will_add_number:
        for i in range(will_add_number, M + 1):
            stack.append(i)
            will_add_number += 1
            answer.append('+')
        stack.pop()
        answer.append('-')

    elif M == will_add_number:
        will_add_number += 1
        answer.append('+')
        answer.append('-')

    else:
        if stack:
            if stack[-1] == M:
                stack.pop()
                answer.append('-')
            else:
                print("NO")
                exit()
        else:
            print("NO")
            exit()

for value in answer:
    print(value)
