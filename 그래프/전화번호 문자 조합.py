def solution(data):
    # 매개변수 : 조합을 시작할 자리수, 만든 정답.
    def dfs(index, answer):
        # 만든 정답과 입력값의 길이가 같고(자리수) 기존에 없던 정답이라면 백트래킹.
        if len(answer) == len(data) and answer not in result:
            result.append(answer)
            return
        # 정답을 만들기 위해 조합.
        # 매개변수로 받은 시작 ~ 자리수 까지.
        for i in range(index, len(data)):
            # 입력받은 데이터에 해당하는 문자들을 하나하나 대입
            for j in num[data[i]]:
                # 다음 인덱스, 만든 정답에 j를 붙혀줌.
                dfs(i + 1, answer + j)

    num = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    result = []
    dfs(0, "")
    return result


if __name__ == "__main__":
    print(solution("23"))
