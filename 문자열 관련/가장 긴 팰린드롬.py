def solution(s: str) -> str:
    # 문자열이 하나이거나 전체 문자열이 팰린드롬 일때는 바로 리턴
    if len(s) < 2 or s == s[::-1]:
        return s

    answer = ""
    for i in range(len(s) - 1):
        # 홀수
        odd = extends(s, i, i + 1)
        # 짝수
        even = extends(s, i, i + 2)

        if len(odd) == len(even):
            pass
        elif len(odd) > len(even):
            if len(odd) > len(answer):
                answer = odd
        else:
            if len(even) > len(answer):
                answer = even
    return answer


def extends(s: str, left: int, right: int) -> str:
    # 리스트 범위를 벗어나지 않고, 좌 우가 같다면
    while left >= 0 and right < len(s) and s[left] == s[right]:
        # 좌 우로 한칸씩 투포인터를 넓힘
        left -= 1
        right += 1
    # 마지막에 조건이 틀려도 한칸씩 더 이동하기에
    # left는 +1을 해서 이전 요소를 가리킬수 있도록 하고 right도 이전요소를 가리키게 함.
    # => a[i:j]일때 i는 포함, j는 미포함(-1)
    return s[left + 1:right]


def solution2(s: str) -> str:
    # 문자열이 하나이거나 전체 문자열이 팰린드롬 일때는 바로 리턴
    if len(s) < 2 or s == s[::-1]:
        return s

    answer = ""
    # 맨 앞에서부터 슬라이드 윈도우를 이동, 오른쪽으로 이동하며 탐색
    for i in range(len(s) - 1):
        # 3개중 길이가 가장 긴것을 answer에 넣음.
        answer = max(extends(s, i, i + 1), extends(s, i, i + 2), answer, key=len)
    return answer

print(solution("1123454321"))
print(solution("11234543212"))
print(solution("babad"))
print(solution2("1123454321"))
print(solution2("11234543212"))
print(solution2("babad"))
