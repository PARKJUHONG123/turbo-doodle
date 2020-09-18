from collections import deque

def bfs(graph, root, length):
    visited = [-1 for _ in range(length + 1)]
    count = 0
    queue = deque([[root, count]])

    while queue:
        value = queue.popleft()
        n = value[0]
        count = value[1]

        if visited[n] == -1:
            visited[n] = count
            count += 1
            for element in graph[n]:
                queue.append([element, count])
    return visited

def dfs(graph, root, length):
    visited = [-1 for _ in range(length + 1)]
    count = 0
    queue = deque([[root, count]])

    while queue:
        value = queue.popleft()
        n = value[0]
        count = value[1]

        if visited[n] == -1:
            visited[n] = count
            count += 1
            for element in graph[n]:
                queue.append([element, count])
    return visited

def solution(n, edge):
    answer = 0
    graph = {} #dict

    for value in edge:
        if value[0] not in graph:
            graph[value[0]] = [value[1]]
        else:
            graph[value[0]].append(value[1])

        if value[1] not in graph:
            graph[value[1]] = [value[0]]
        else:
            graph[value[1]].append(value[0])
    print(bfs(graph, 1, n))
    return answer

def main():
    n = 6
    vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    solution(n, vertex)

if __name__ == "__main__":
    main()