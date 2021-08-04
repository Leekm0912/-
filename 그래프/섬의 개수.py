from CheckTime import CheckTime


@CheckTime
def solution1(data):
    temp1 = []
    for d in data:
        temp1.append(list(d))
    data = temp1

    count = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            # 모든 육지 탐색 후 카운트 1 증가
            if data[i][j] == "1":
                dfs(data, i, j)
                count += 1
    print(data)
    return count


# 만나는 모든 땅을 *로 만들어줌.
def dfs(data, i, j):
    # 세로 범위를 벗어났거나
    # 가로 범위를 벗어났거나
    # 땅이 아니면 종료
    if i < 0 or i >= len(data) or \
            j < 0 or j >= len(data[0]) or \
            data[i][j] != '1':
        return
    data[i][j] = "*"
    # 동서남북 탐색
    dfs(data, i + 1, j)
    dfs(data, i - 1, j)
    dfs(data, i, j + 1)
    dfs(data, i, j - 1)


@CheckTime
def solution2(data):
    temp1 = []
    for d in data:
        temp1.append(list(d))
    data = temp1

    stack = []
    count = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "1":
                stack.append((i, j))
                while stack:
                    in_i, in_j = stack.pop()
                    if in_i < 0 or in_i >= len(data) or \
                            in_j < 0 or in_j >= len(data[0]) or \
                            data[in_i][in_j] != "1":
                        continue
                    data[in_i][in_j] = "*"
                    stack.append((in_i + 1, in_j))
                    stack.append((in_i - 1, in_j))
                    stack.append((in_i, in_j + 1))
                    stack.append((in_i, in_j - 1))
                count += 1
    print(data)
    return count


if __name__ == "__main__":
    print(solution1([
        "11110",
        "11010",
        "11000",
        "00000"
    ]))

    print(solution2([
        "11110",
        "11010",
        "11000",
        "00000"
    ]))
