# 배열을 입력받아 output[i]가
# 자신을 제외한 나머지 요소의 곱셈 결과가 되도록 출력하라
# 나눗셈을 하지말고 O(n)에 풀이
def solution1(data):
    out = []
    p = 1
    # 왼쪽 곱셈
    for i in range(0, len(data)):
        # p를 넣고
        out.append(p)
        # 왼쪽 값을 곱한다.
        p = p * data[i]
    p = 1
    for i in range(len(data) - 1, 0 - 1, -1):
        out[i] = out[i] * p
        p = p * data[i]
    return out


print(solution1([1, 2, 3, 4]))
