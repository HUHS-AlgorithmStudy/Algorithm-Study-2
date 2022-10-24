from queue import PriorityQueue


def making_graph(N, road):
    graph = {}  # 주어진 마을과 도로의 모양을 나타냄 {1: {2: 1}}이면 1번 나라에서 2번 나라로 갈 때 1시간이 걸린다는 뜻
    distance = {}  # 1번 마을로부터 떨어진 거리
    for i in range(N):
        graph[i + 1] = {}
        distance[i + 1] = float('inf')

    for j in range(N):
        for x in range(len(road)):
            for y in range(len(road[x])):
                if road[x][0] == (j + 1):
                    # 여러 개의 거리 중 걸리는 시간이 더 짧은 것을 선택하기 위한 조건
                    if (road[x][1] not in graph[j + 1]) or (graph[j + 1][road[x][1]] > road[x][2]):
                        graph[j + 1].update({road[x][1]: road[x][2]})
                        # 방향이 없는 그래프이므로 반대 방향의 나라 기준에서도 거리 기재
                        graph[road[x][1]].update({(j + 1): road[x][2]})
    return graph, distance


def solution(N, road, K):
    priority_queue = PriorityQueue()  # 맨 앞의 값을 효율적으로 얻기 위해 PriorityQueue 사용
    graph, distance = making_graph(N, road)
    distance[1] = 0  # 1번 나라는 자기 나라에 갈 때 걸리는 시간이 0시간
    priority_queue.put(1)
    while priority_queue.qsize() != 0:  # priority_queue가 빌 때까지
        target_country = priority_queue.get()  # 맨 앞의 나라 기준으로 살펴본다
        for key, value in graph[target_country].items():
            # 이미 저장된 시간보다 새로 들어온 시간이 더 오래 걸리면 스킵한다.
            if distance[key] < distance[target_country] + value:
                continue
            distance[key] = distance[target_country] + value
            priority_queue.put(key)  # 전 나라와 연결된 나라를 queue에 넣어준다.

    counter = 0
    for result in distance.values():  # 최종적으로 나온 시간들 중 K시간 이하인 것들의 개수를 구한다.
        if result <= K:
            counter += 1
    return counter
