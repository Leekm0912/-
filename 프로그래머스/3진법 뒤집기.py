def solution(n):
    result = ""
    while n >= 3:
        # n을 3으로나눈 몫은 n에, 나머지는 temp에 저장
        n, temp = divmod(n, 3)
        # 나머지를 저장
        result += str(temp)
    # 남은 n값 추가해주면 3진수 뒤집어서 저장됨.
    result += str(n)

    # 지수와 정답 초기화
    exponent = 0
    answer = 0
    # 계산할때는 다시 뒤집어서 첫번째로 오는게 3^0 자리부터 오도록.
    for i in result[::-1]:
        # (3의 지수제곱) * i
        answer += (3 ** exponent) * int(i)
        # 지수부분 올려줌
        exponent += 1
    return answer
