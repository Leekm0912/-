def solution(prices):
    n = len(prices)
    # 1. answer를 prices 길이와 맞춘다.
    answer = [0] * n
    # 2. 스택 생성
    st = []
    # 3. 0 ~ n-1 초까지 순회
    for now_time in range(n):
        # 3-1. 스택이 비어있지 않고,
        # 스택 가장 위(마지막에 저장된 시간)의 값이 현재가격보다 크다면  반복
        while st and prices[st[-1]] > prices[now_time]:
            # 3-1-1. 스택에서 마지막에 저장된 시간 top 꺼냄
            top = st.pop()
            # 3-1-2. answer[top]에 now_time - top을 저장
            answer[top] = now_time - top
        # 3-2. 스택에 현재 시간 i 저장
        st.append(now_time)
    # 4. 만약 스택이 남아있다면, 스택이 빌 때까지 다음 반복
    while st:
        # 4-1. 스택에서 마지막에 저장된 시간 top 꺼냄
        # 4-2. answer[top]에 가장 마지막 시간 n - i 에서 top을 뺸 시간 저장
        top = st.pop()
        answer[top] = n - 1 - top

    return answer
