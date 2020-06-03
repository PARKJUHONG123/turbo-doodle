T = int(input())

for i in range(T):
    n = int(input())
    lock = [True for _ in range(n + 1)]
    for j in range(n + 1):
        for k in range(n + 1):
            if j * k < n + 1:
                if lock[j * k] == True:
                    lock[j * k] = False
                else :
                    lock[j * k] = True

    count = 0
    for i in range(1, n + 1) :
        if lock[i] == False:
            count += 1
    print(count)
