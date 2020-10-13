import math
INF = math.inf

def solution(depar, hub, dest, roads):
    dp = [[INF for _ in range(2)] for _ in range(2)]
    cities = dict()
    city_index = 0
    for road in roads:
        a, b = -1, -1
        if road[0] in cities:
            a = cities[road[0]]
        else:
            cities[road[0]] = city_index
            a = city_index
            city_index += 1

        if road[1] in cities:
            b = cities[road[1]]
        else:
            cities[road[1]] = city_index
            b = city_index
            city_index += 1

        dp_length = len(dp)
        if dp_length < city_index:
            new_length = 2 * dp_length
            new_dp = [[INF for _ in range(new_length)] for _ in range(new_length)]
            for i in range(dp_length):
                for j in range(dp_length):
                    new_dp[i][j] = dp[i][j]
            dp = new_dp
        dp[a][b] = 1

    for k in range(city_index):
        for i in range(city_index):
            for j in range(city_index):
                if dp[i][k] != INF and dp[k][j] != INF:
                    dp[i][j] = (dp[i][k] + dp[k][j]) % 10007

    d_h = dp[cities[depar]][cities[hub]]
    h_d = dp[cities[hub]][cities[dest]]
    value = d_h * h_d
    if value == INF:
        print(0)
    else:
        print(value)

depar, hub, dest, roads = "SEOUL",   "DAEGU",   "YEOSU",   [["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","DAEJEON"],["SEOUL","ULSAN"],["DAEJEON","DAEGU"],["GWANGJU","BUSAN"],["DAEGU","GWANGJU"],["DAEGU","BUSAN"],["ULSAN","DAEGU"],["GWANGJU","YEOSU"],["BUSAN","YEOSU"]]
solution(depar, hub, dest, roads)
