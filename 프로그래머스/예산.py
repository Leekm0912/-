from codingTest.CheckTime import CheckTime


@CheckTime
def solution(d, budget):
    answer = 0

    d.sort(reverse=True)
    while d and budget > 0:
        now = d.pop()
        if now <= budget:
            budget -= now
            answer += 1
        else:
            break
    return answer


if __name__ == '__main__':
    solution([1, 3, 2, 5, 4], 9)
    solution([2, 2, 3, 3], 10)
