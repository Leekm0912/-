from codingTest import CheckTime


@CheckTime.CheckTime
def solution(data) -> bool:
    stack = []
    # 각각 매핑되는 괄호 지정
    table = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    for i in data:
        # ) } ] 이외의 값들은 모두 넣음
        if i not in table:
            stack.append(i)
        # 스택이 비어있다는건 ) } ]로 시작했다는 뜻.
        # 그리고 ) } ] 일때 여기로 넘어오는데, pop한 값이 매핑되지 않는다면 순서가 맞지 않는다는 뜻.
        elif not stack or table[i] != stack.pop():
            return False
    # 처리가 정상적으로 완료됐다면 stack은 비어있어야 함.
    return len(stack) == 0


if __name__ == "__main__":
    print(solution("()[]{}"))
    print(solution("(]{}"))
