import sys

N = int(sys.stdin.readline())

switch = [[0 for _ in range(N)] for _ in range(2)]
target = [0 for _ in range(N)]

tmp = sys.stdin.readline()
for i in range(N):
    switch[0][i] = int(tmp[i])
    switch[1][i] = int(tmp[i])

tmp = sys.stdin.readline()
for i in range(N):
    target[i] = int(tmp[i])

def switching(sw_index, index):
    if 0 <= index - 1 < N:
        switch[sw_index][index - 1] = (0 if switch[sw_index][index - 1] == 1 else 1)
    if 0 <= index < N:
        switch[sw_index][index] = (0 if switch[sw_index][index] == 1 else 1)
    if 0 <= index + 1 < N:
        switch[sw_index][index + 1] = (0 if switch[sw_index][index + 1] == 1 else 1)

fc_count, fnc_count = 0, 0
for i in range(N):
    if i == 0:
        fc_count += 1
        switching(0, i)

    else:
        if switch[0][i - 1] != target[i - 1]:
            fc_count += 1
            switching(0, i)
        if switch[1][i - 1] != target[i - 1]:
            fnc_count += 1
            switching(1, i)

fc_token, fnc_token = False, False
for i in range(N):
    if switch[0][i] != target[i]:
        fc_token = True
    if switch[1][i] != target[i]:
        fnc_token = True

if fc_token:
    if fnc_token:
        print(-1)
    else:
        print(fnc_count)
else:
    if fnc_token:
        print(fc_count)
    else:
        print(min(fc_count, fnc_count))