def solution(data):
    def dfs(index, path):
        if len(path) == len(data):
            answer.append(path)
            return

        for i in range(index, len(data)):
            for j in num[data[i]]:
                dfs(i + 1, path + j)

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
    answer = []
    dfs(0, "")
    return answer


if __name__ == "__main__":
    print(solution("23"))
