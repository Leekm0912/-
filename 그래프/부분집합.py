def solution(nums):
    answer = []

    def dfs(save, index):
        if save not in answer:
            answer.append(save[:])

        for i in range(index, len(nums)):
            save.append(nums[i])
            dfs(save, i+1)
            save.pop()

    dfs([], 0)
    return answer


if __name__ == "__main__":
    print(solution([1, 2, 3]))
