def solution(n, k):
    answer = []

    def dfs(index, now):
        if len(now) == k:
            print(now)
            answer.append(now[:])
            return

        for i in range(index, n + 1):
            now.append(i)
            dfs(i + 1, now)
            now.pop()

    dfs(1, [])
    return answer


if __name__ == "__main__":
    print(solution(4, 2))
