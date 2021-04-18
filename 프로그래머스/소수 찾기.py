def solution(n):
    answer = 0
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * (n + 1)

    # 1. n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    # 2. 1은 제거(여기서는 무시했음)
    # 3. 지워지지 않은 수 중 제일 작은 2를 소수로 채택하고, 나머지 2의 배수를 모두 지운다.
    # 4. 지워지지 않은 수 중 제일 작은 3을 소수로 채택하고, 나머지 3의 배수를 모두 지운다.
    # 5. 지워지지 않은 수 중 제일 작은 5를 소수로 채택하고, 나머지 5의 배수를 모두 지운다.
    # 6. 반복
    sqrt = int(n ** 0.5)
    for i in range(2, sqrt + 1):
        # i가 소수인 경우
        if sieve[i]:
            # i이후 i의 모든 배수들을 False 판정
            for j in range(i + i, n + 1, i):
                sieve[j] = False

    # 소수 숫자 카운트
    for i in range(2, n + 1):
        if sieve[i]:
            answer += 1

    return answer
