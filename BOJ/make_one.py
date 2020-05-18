num = int(input())
result = [0 for _ in range(num + 1)]

for i in range(1, num + 1):
    if i == 1:
        result[i] = 0
        continue
    result[i] = result[i-1] + 1
    j = i // 3
    if i % 3 == 0 and result[j] + 1 < result[i]:
        result[i] = result[j] + 1
    j = i // 2
    if i % 2 == 0 and result[j] + 1 < result[i]:
        result[i] = result[j] + 1

print(result[num])
