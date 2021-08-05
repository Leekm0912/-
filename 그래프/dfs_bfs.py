def recursive_dfs(graph, v, discovered=[]):
    discovered.append(v)

    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs(graph, w, discovered)
    return discovered


def iterative_dfs(graph, v):
    stack = [v]
    discovered = []

    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered


def bfs(graph, start_v):
    queue = [start_v]
    discovered = [start_v]

    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered


if __name__ == "__main__":
    graph = {
        1: [2, 3, 4],
        2: [5],
        3: [5],
        4: [],
        5: [6, 7],
        6: [],
        7: [3],
    }

    print(recursive_dfs(graph, 1))
    print(iterative_dfs(graph, 1))
    print(bfs(graph, 1))
