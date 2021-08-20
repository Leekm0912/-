from CheckTime import CheckTime


@CheckTime
def solution(lottos, win_nums):
    answer = 0
    num_of_zero = 0

    for i in lottos:
        if i in win_nums:
            answer += 1
        elif i == 0:
            num_of_zero += 1

    # 최저 점수는 0에 들어가는 번호가 아무거도 안맞았을때.
    # 7을 빼준 이유는, answer가 6일때, 즉 모두 맞았을때가 1등이므로 7 - 6 = 1등
    min_answer = 7 - answer
    if min_answer > 6:
        min_answer = 6

    # 최고 점수는 0에 들어가는 번호가 모두 맞았을때.
    # 순위는 값이 낮을수록 높으므로 0의 개수만큼 빼줌.
    max_answer = min_answer - num_of_zero
    if max_answer < 1:
        max_answer = 1
    return [max_answer, min_answer]


if __name__ == "__main__":
    solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])
    solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])
    solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])
