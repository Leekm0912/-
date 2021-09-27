 import heapq
from collections import defaultdict

import CheckTime


@CheckTime.CheckTime
def solution1(n, edges, src, dst, K):
    graph = defaultdict(list)
    # u : 출발지
    # v : 도착지
    # w : 가격
    for u, v, w in edges:
        graph[u].append((v, w))
    print(graph)
    # 우선순위 큐 변수 [(가격, 정점, 남은 카운트 제한)]
    queue = [(0, src, K)]
    save_price = defaultdict(lambda: -1)

    while queue:
        price, node, now_k = heapq.heappop(queue)
        if now_k >= 0:
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(queue, (alt, v, now_k - 1))
                if save_price[v] == -1 or alt < save_price[v]:
                    save_price[v] = alt
    return save_price[dst]


@CheckTime.CheckTime
def solution2(n, edges, src, dst, K):
    graph = defaultdict(list)
    # u : 출발지
    # v : 도착지
    # w : 가격
    for u, v, w in edges:
        graph[u].append((v, w))
    print(graph)
    # 우선순위 큐 변수 [(가격, 정점, 남은 카운트 제한)]
    queue = [(0, src, K)]

    while queue:
        price, node, now_k = heapq.heappop(queue)
        if node == dst:
            return price
        if now_k >= 0:
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(queue, (alt, v, now_k - 1))
    return -1


if __name__ == "__main__":
    solution1(n=3, edges=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, K=0)
    solution2(n=3, edges=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, K=0)
    solution1(n=3, edges=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, K=1)
    solution2(n=3, edges=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, K=1)
