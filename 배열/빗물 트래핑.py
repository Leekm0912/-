def solution1(data: list) -> int:
    answer = 0
    left = 0
    right = len(data) - 1

    left_max = data[left]
    right_max = data[right]
    while left < right:
        left_max, right_max = max(data[left], left_max), \
                              max(data[right], right_max)
        if left_max <= right_max:
            answer += left_max - data[left]
            left += 1
        else:
            answer += right_max - data[right]
            right -= 1
    return answer


def solution2(data: list) -> int:
    stack = []
    answer = 0
    num = 0
    print("start!"
          "")
    for i in range(len(data)):
        print(f"===================i : {num}===================")
        # 변곡점(내려가는 경우)을 만나는 경우
        # 스택이 비어있지 않고, 현재 i 위치의 값이 스택의 값보다 크다면(내려간다면)
        while stack and data[i] > data[stack[-1]]:
            # 스택에서 꺼냄
            top = stack.pop()
            print("\tpop :", top)
            print("\ttop :", top, end=", ")
            if not len(stack):
                print("\t break")
                break

            # 이전과의 차이만큼 물 높이 처리
            distance = i - stack[-1] - 1  # 가로
            waters = min(data[i], data[stack[-1]]) - data[top]  # 세로
            print("distance :", distance, "waters :", waters)
            answer += distance * waters

        stack.append(i)
        print(f"\tappend:{i}")
        print("stack:", stack, "answer:", answer)

        num += 1
    return answer


# print(solution1([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(solution2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
