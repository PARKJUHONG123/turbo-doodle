import sys

def before_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i - 1] <= a[i]: #오른쪽부터 x, y 중 x 가 크면 왼쪽으로 index "i" 이동 -> 1 3 5 4 2 에서 a[i - 1] == 5 and a[i] == 4
        i -= 1
    if i <= 0:
        return False

    j = len(a) - 1
    while a[i - 1] <= a[j]: # 1 3 5 4 2 에서 a[i - 1] 인 5보다 a[4] 인 4가 작으므로 a[j] 는 4를 말한다
        j -= 1
    a[i - 1], a[j] = a[j], a[i - 1] # 1 3 4 2 5

    j = len(a) - 1
    while i < j: # i == 3, j == 4
        a[i], a[j] = a[j], a[i] # 1 3 4 5 2
        i += 1
        j -= 1

    return True


n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

if before_permutation(a):
    print(' '.join(map(str, a)))
else:
    print(-1)

