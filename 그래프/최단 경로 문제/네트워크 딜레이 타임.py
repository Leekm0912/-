import heapq
from collections import defaultdict

import CheckTime


@CheckTime.CheckTime
# times : 노드 리스트
# N : 전체 노드의 개수
# K : 출발지점
def solution(times, N, K):
    graph = defaultdict(list)
    # u : 출발지
    # v : 도착지
    # w : 소요시간
    for u, v, w in times:
        graph[u].append((v, w))
    # 우선순위 큐 변수 [(소요시간, 정점)]
    # 1. 출발 노드 설정
    # 2. 출발 노드를 기준으로 각 노드의 최소 비용을 저장
    Q = [(0, K)]
    dist = defaultdict(int)

    while Q:
        # 현재 저장된 노드 중 가장 비용이 적은 노드 선택
        time, node = heapq.heappop(Q)
        # 방문하지 않았다면
        if node not in dist:
            # 방문처리하고 시간 저장
            dist[node] = time
            # 현재 노드에서 갈 수 있는 노드를 거쳐 노드 값 업데이트
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))
    if len(dist) == N:
        return max(dist.values())
    return -1


@CheckTime.CheckTime
# times : 노드 리스트
# N : 전체 노드의 개수
# K : 출발지점
def solution2(times, N, K):
    graph = defaultdict(list)
    # u : 출발지
    # v : 도착지
    # w : 소요시간
    for u, v, w in times:
        graph[u].append((v, w))
    # 우선순위 큐 변수 [(소요시간, 정점)]
    # 1. 출발 노드 설정
    queue = [(0, K)]
    dist = defaultdict(lambda: -1)
    while queue:
        # 2. 현재 저장된 노드에서 가장 비용이 적은 노드 선택.
        time, node = heapq.heappop(queue)
        # 3. 선택된 노드에 방문하지 않았다면 방문처리하고 시간 저장
        if node not in dist:
            dist[node] = time
        # 4. 선택된 노드를 거쳐서 특정한 노드로 가는 경우를 고려하여 최소 비용을 갱신.
        for v, w in graph[node]:
            # 비용 계산
            alt = time + w
            # 현재 노드와 계산한 비용을 queue에 저장. (2번과정에서 사용)
            heapq.heappush(queue, (alt, v))
            # 만약 현재 방문하지 않았거나(초기값 -1), 거쳐 가는 비용이 더 작을때 갱신.
            if dist[v] == -1 or alt < dist[v]:
                dist[v] = alt
    if len(dist) == N:
        return max(dist.values())
    return -1


if __name__ == "__main__":
    solution([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2)
    solution2([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2)
    solution([[3, 1, 8], [3, 2, 6], [2, 1, 2], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 1, 1]], N=8,
             K=3)
    solution2([[3, 1, 8], [3, 2, 6], [2, 1, 2], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 1, 1]], N=8,
              K=3)

    solution([[2, 3, 1], [3, 4, 1]], 4, 2)
    solution2([[2, 3, 1], [3, 4, 1]], 4, 2)
