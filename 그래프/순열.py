import itertools


def solution(data):
    result = []
    prev = []

    def dfs(elements):
        # elements의 len이 0이면 순환 종료.
        if len(elements) == 0:
            result.append(prev[:])
        # 요소를 하나하나 추가시킴.
        for e in elements:
            # ele 복사
            next = elements[:]
            # next에서 e를 빼고 prev에 넣음.
            next.remove(e)
            prev.append(e)
            # 순환호출
            dfs(next)
            # 순환호출이 끝나면 prev를 pop시켜 다음 작업 준비.
            prev.pop()

    dfs(data)
    return result


def solution2(data):
    return list(map(list, itertools.permutations(data)))


if __name__ == "__main__":
    print(solution([1, 2, 3]))
    print(solution2([1, 2, 3]))
