from CheckTime import  CheckTime


@CheckTime
def solution(str)->int:
    result = ""
    temp = ""
    for c in str:
        if c not in temp:
            temp += c
            # 만난 가장 긴 문자열 중 처음을 저장하는 방식. 이후에 같은 길이가 나와도 무시됨.
            if len(temp) > len(result):
                result = temp
        else:
            temp = c
    print(result)
    return len(result)


if __name__ == "__main__":
    print(solution("abcabcbb"))
    print(solution("bbbbbb"))
    print(solution("pwwkew"))