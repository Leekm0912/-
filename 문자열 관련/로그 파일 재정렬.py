def solution(logs: list) -> list:
    letters = list()
    digits = list()
    for log in logs:
        # 숫자로 시작하는지, 문자로 시작하는지 구분
        if not log.split(" ")[1].isdigit():
            letters.append(log)
        else:
            digits.append(log)

    # 문자로 시작하는 로그는 문자순으로 정렬, 문자가 같다면 식별자순으로 정렬
    letters.sort(key=lambda x: (x.split(" ")[1:], x.split(" ")[0]))
    # 문자로그와 숫자로그를 합쳐서 리턴(문자 로그가 먼저옴)
    return letters + digits


print(solution(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))
