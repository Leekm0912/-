from codingTest import CheckTime


@CheckTime.CheckTime
def solution(data):
    answer = []

    for i, temp in enumerate(data):
        count = 1
        while True:
            try:
                if temp < data[i + count]:
                    break
            except:
                count = 0
                break
            count += 1
        answer.append(count)
    return answer


if __name__ == "__main__":
    solution([73, 74, 75, 71, 69, 72, 76, 73])
