def solution(candidates, target):
    answer = []

    def dfs(now: list):
        if sum(now) > target:
            return
        elif sum(now) == target and sorted(now) not in answer:
            answer.append(sorted(now))
            return

        for i in range(len(candidates)):
            now.append(candidates[i])
            dfs(now)
            now.pop()

    dfs([])
    return answer


if __name__ == "__main__":
    print(solution([2, 3, 6, 7], 7))
    print(solution([2, 3, 5], 8))
