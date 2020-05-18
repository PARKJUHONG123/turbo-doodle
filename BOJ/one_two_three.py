num = int(input())

def get_count(num, cur, count):
    if (cur == num):
        count[0] = count[0] + 1
        return
    if (cur + 1 <= num):
        get_count(num, cur + 1, count)
    if (cur + 2 <= num):
        get_count(num, cur + 2, count)
    if (cur + 3 <= num):
        get_count(num, cur + 3, count)

answer = []
for i in range(num):
    temp = int(input())
    count = [0]
    get_count(temp, 0, count)
    answer += count

for i in range(len(answer)):
    print(answer[i])