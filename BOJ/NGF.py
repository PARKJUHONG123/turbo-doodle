import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))
F = dict()
for value in A:
    if value in F:
        F[value] += 1
    else:
        F[value] = 1

stack = list()
stack.append(A[-1])
answer = [-1]
for i in reversed(range(N - 1)):
    if stack:
        if F[A[i]] < F[stack[-1]]:
            answer.append(stack[-1])
        else:
            while F[A[i]] >= F[stack[-1]]:
                stack.pop()
                if not stack:
                    answer.append(-1)
                    break
            if stack:
                answer.append(stack[-1])
    else:
        answer.append(-1)
    stack.append(A[i])

print(*answer[::-1])