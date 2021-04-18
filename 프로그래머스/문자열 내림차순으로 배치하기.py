def solution(s):
    # 초기화
    answer = ""
    temp = []

    for i in s:
        # 아스키 코드로 변환
        temp.append(ord(i))
    # 내림차순으로 정렬
    temp.sort(reverse=True)

    for i in temp:
        # 문자로 변환
        answer += chr(i)
    return answer
