from CheckTime import CheckTime


@CheckTime
def solution(nums):
    global answer
    answer = 0
    save = []

    def dfs(index):
        global answer
        if len(nums) / 2 == len(save):
            save_len = len(set(save))
            if answer < save_len:
                answer = save_len
            return

        for i in range(index, len(nums)):
            save.append(nums[i])
            dfs(i + 1)
            save.pop()

    dfs(0)
    return answer


if __name__ == "__main__":
    solution([3, 1, 2, 3])
    solution([3, 3, 3, 2, 2, 4])
    solution([3, 3, 3, 2, 2, 2])
