def next_permutations(a):
    i = len(a) - 1
    while i > 0 and a[i - 1] >= a[i]: #오른쪽부터 x, y 중 x 가 크면 왼쪽으로 index "i" 이동 -> 1 3 5 4 2 에서 a[i] == 5 and a[i - 1] == 3
        i -= 1
    if i <= 0:
        return False

    j = len(a) - 1
    while a[i - 1] >= a[j]: # 1 3 5 4 2 에서 a[i - 1] 인 3보다 a[4] 인 2가 작으므로 a[j] 는 4를 말한다
        j -= 1
    a[i - 1], a[j] = a[j], a[i - 1] # 1 4 5 3 2

    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i] # 1 4 2 3 5
        i += 1
        j -= 1

    return True


n = int(input())
a = list(map(int, input().split()))

if next_permutations(a):
    print(' '.join(map(str, a)))
else:
    print(-1)

