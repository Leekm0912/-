def solution(s, n):
    answer = ''
    # A = 65 ~ Z = 90
    # a = 97 ~ z = 122
    # 공백 = 32
    for i in s:
        # 아스키코드 변환
        code = ord(i)

        # 공백 처리
        if code == 32:
            answer += " "
            continue

        # A~Z범위 처리
        if 65 <= code <= 90:
            # 만약 A~Z범위를 벗어난다면
            if code + n > 90:
                # A의 아스키코드 + n을더한 아스키코드 - Z의 아스키코드
                code = 64 + (code + n) - 90
            else:
                code += n
        # a~z범위 처리
        if 97 <= code <= 122:
            # 위와 동일함
            if code + n > 122:
                code = 96 + (code + n) - 122
            else:
                code += n
        # 다시 아스키코드를 문자로 바꾸어서 정답문자열에 추가
        answer += chr(code)
    return answer
