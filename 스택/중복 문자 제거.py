from codingTest import CheckTime


@CheckTime.CheckTime
def solution(data: str) -> str:
    return "".join(sorted((list(set(list(data))))))


@CheckTime.CheckTime
def solution2(data: str) -> str:
    return "".join(list(set(list(data))))


if __name__ == "__main__":
    solution("bcabc")
    solution("cbacdcbc")
    solution2("bcabc")
    solution2("cbacdcbc")
