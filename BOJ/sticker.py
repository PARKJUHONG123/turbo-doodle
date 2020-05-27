count = int(input())

for _ in range(count):
    n = int(input())
    a = [0 for _ in range(n)]
    b = [0 for _ in range(n)]
    d_a = [0 for _ in range(n)]
    d_b = [0 for _ in range(n)]

    temp = input()
    temp = temp.split()
    for i in range(n) :
        a[i] = int(temp[i])

    temp = input()
    temp = temp.split()
    for i in range(n) :
        b[i] = int(temp[i])

    d_a[0] = a[0]
    d_b[0] = b[0]

    for i in range(1, n) :
        max_a = 0
        max_b = 0

        if (i == 1) :
            max_a = d_b[i - 1]
            max_b = d_a[i - 1]
        else :
            max_a = max(d_a[i - 2], d_b[i - 1], d_b[i - 2])
            max_b = max(d_b[i - 2], d_a[i - 1], d_a[i - 2])
        d_a[i] = a[i] + max_a
        d_b[i] = b[i] + max_b

    print(max(d_a[-1], d_b[-1]))