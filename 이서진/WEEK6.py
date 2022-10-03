import heapq as hq


def dikjstra(graph, start, dist):
    # 시작 노드 초기화
    heap = []
    hq.heappush(heap, (0, start))
    dist[start] = 0

    while heap:
        cost, current = hq.heappop(heap)
        if dist[current] < cost:
            continue
        for g in graph[current]:  # g[0] = g cost, g[1] = graph
            if cost + g[1] < dist[g[0]]:  # cost가 지금 저장된 시간보다 적다면
                dist[g[0]] = cost + g[1]  # 마을까지 가는 데 걸리는 최소 시간을 cost로 변경
                hq.heappush(heap, (cost + g[1], g[0]))  # heap에 저장

    return dist


def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N + 1)]

    # 인접한 마을까지 걸리는 시간들을 그래프로 구성한다.
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    # 가장 큰 값으로 정한다. (dist = distance)
    dist = [float('inf')] * (N + 1)

    # 다익스트라 알고리즘을 이용해 1번 마을부터 각 마을까지 가는 최소 시간을 구해 dist에 저장한다.
    dist = dikjstra(graph, 1, dist)

    # 모든 마을을 돌며 각 마을까지의 최소 시간이 요청된 시간보다 적다면 answer을 하나씩 더한다.
    for i in range(1, N + 1):
        if dist[i] <= K:
            answer += 1

    return answer
