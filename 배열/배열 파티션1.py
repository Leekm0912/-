def solution1(data):
    # 정렬 후 비교
    data.sort()
    pair = []
    answer = 0

    for i in data:
        pair.append(i)
        if len(pair) == 2:
            answer += min(pair)
            pair = []
    return answer


def solution2(data):
    # 짝수번째 값 계산
    answer = 0
    for i, v in enumerate(data):
        if i % 2 == 0:
            answer += v
    return answer


def solution3(data: list):
    # 슬라이싱 구문 [::2] 는 2칸씩 건너뛰므로 짝수번째를 계산하는 것과 같음
    return sum(sorted(data)[::2])


print(solution1([1, 4, 3, 2]))
print(solution2([1, 4, 3, 2]))
print(solution3([1, 4, 3, 2]))
