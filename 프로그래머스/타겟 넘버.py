def solution(numbers, target):
    global answer
    answer = 0
    answer_list = []

    def dfs(num: list, index):
        global answer
        if len(num) == len(numbers) and sum(num) == target and num not in answer_list:
            answer += 1
            print(num, sum(num))
            answer_list.append(num)
            print(answer)
            return
        if len(num) == len(numbers):
            return

        dfs(num + [numbers[index]], index + 1)
        dfs(num + [-numbers[index]], index + 1)

    dfs([], 0)
    # print(answer_list)
    return answer


if __name__ == "__main__":
    print(solution([1, 1, 1, 1, 1], 3))
    print(solution([3, 5, 2, 9, 7, 4], 4))
