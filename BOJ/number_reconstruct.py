import sys

A, B = sys.stdin.readline().split()
A_list = list()
int_B = int(B)
N = len(A)
for i in range(N):
    A_list.append(A[i])

def brute(result):
    global max_result
    if not (False in visited):
        if result[0] != '0':
            int_result = int(result)
            if int_result <= int_B:
                max_result = max(max_result, int_result)
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                brute(result + A[i])
                visited[i] = False

if N > len(B):
    print(-1)
elif N == len(B):
    visited = [False for _ in range(N)]
    max_result = -1
    brute('')
    print(max_result)
else:
    A = A_list
    A.sort(reverse = True)
    if A[0] == '0':
        print(-1)
    else:
        print(''.join(A))

