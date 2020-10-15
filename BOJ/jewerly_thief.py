import sys
from queue import PriorityQueue
N, K = map(int, sys.stdin.readline().split())
max_value = 2000000
stuff_list = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    stuff_list.append([x, y])
for _ in range(K):
    x, y = int(sys.stdin.readline()), max_value
    stuff_list.append([x, y])
stuff_list.sort()

answer = 0
pq = PriorityQueue()
for value in stuff_list: # 사이즈가 작은 보석들과 가방 순서대로
    if value[1] != max_value: # 가방이 아닌 보석일 경우
        pq.put(-value[1]) # pq 에 보석의 가치를 넣음
    else: # 가방일 경우
        if not pq.empty(): # pq에 보석이 있을 경우
            jewerly = -pq.get() # pq에서 가장 가치가 큰 (-로 가장 큰) 보석을 꺼낸다
            answer += jewerly
print(answer)
