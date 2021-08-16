from codingTest import CheckTime


@CheckTime.CheckTime
def solution(n, data):
    graph = {}
    for a, b in data:
        if a == b:
            return False
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
    print(graph)

    traced = {}

    def dfs(i):
        if i in traced:
            return False

        traced[i] = True
        if i in graph:
            for node in graph[i]:
                if not dfs(node):
                    return False
            traced.pop(i)
        return True

    for node in list(graph):
        if not dfs(node):
            return False
    return True


if __name__ == "__main__":
    solution(2, [[1, 0]])
    solution(2, [[1, 0], [0, 1]])
    solution(20, [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]])
