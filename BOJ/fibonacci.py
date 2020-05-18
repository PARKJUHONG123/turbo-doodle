# 0(1, 0) 1(0, 1) 2 (1, 1) 3 (1, 2) 4 (2, 3) 5(3, 5)
def fib(n):
    if (n == 0) :
        return 1, 0
    elif (n == 1) :
        return 0, 1
    elif (n >= 2) :
        zero = [0 for _ in range(n + 1)]
        one = [0 for _ in range(n + 1)]
        zero[0] = 1
        one[1] = 1
        for i in range(2, n + 1):
            zero[i] = zero[i - 1] + zero[i - 2]
            one[i] = one[i - 1] + one[i - 2]
        return zero[n], one[n]

num = int(input())
zero_answer = [0 for _ in range(num)]
one_answer = [0 for _ in range(num)]

for i in range(num):
    temp = int(input())
    zero, one = fib(temp)
    zero_answer[i] = zero
    one_answer[i] = one

for i in range(num):
    print(zero_answer[i], one_answer[i])