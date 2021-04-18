def solution(number, k):
    # 1. 스택 생성
    stack = []

    # 2. 큰 수가 앞자리가 되게끔 스택에 저장.
    for elem in number:
        # 2-1. 스택이 비어있지 않고,
        # 2-2. 스택의 맨 위의 값이 현재 elem보다 작고, <- 작다면 지워줘야함. 앞자리가 클수록 값이 커지기 때문.
        # 2-3. 지울 횟수가 남았다면.
        while stack and stack[-1] < elem and k > 0:
            # 지울때마다 k의 횟수 감소.
            stack.pop()
            k -= 1
        # 검사를 통과해서 elem이 제일 큰게 확인됐다면 스택에 추가.
        stack.append(elem)

    # 3. 지울횟수가 남았다면 뒤에서부터 잘라줌.
    if(k>0):
        stack = stack[:-k]

    return "".join(stack)