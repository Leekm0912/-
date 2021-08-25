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
    print(graph)
    # 우선순위 큐 변수 [(소요시간, 정점)]
    Q = [(0, K)]
    dist = defaultdict(int)

    while Q:
        time, node = heapq.heappop(Q)
        print("pop(time, node)", (time, node))
        if node not in dist:
            print("now node", node)
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))
                print("push(time, node)", (alt, v))
            print("now Q", Q)
            print("now dist", dist)
    print(dict(dist))
    if len(dist) == N:
        return max(dist.values())
    return -1


if __name__ == "__main__":
    # solution([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2)
    solution([[3, 1, 8], [3, 2, 6], [2, 1, 2], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 1, 1]], N=8,
             K=3)
