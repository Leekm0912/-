# 1. 대문자 -> 소문자
def step1(id):
    return id.lower()


# 2. 소문자, 숫자, 빼기, 밑줄 제외하고 제거
def step2(id):
    result = ""
    for c in id:
        # 알파벳이 아니고, -_.이 아니면 패스 나머지는 추가
        if (not c.isalnum()) and (c != "-" and c != "_" and c != "."):
            pass
        else:
            result += c
    return result


# 3. 마침표가 2번이상 연속된부분을 하나로 치환
def step3(id):
    result = id[0]
    for c in id[1:]:
        print(c)
        # result의 가장 마지막 부분이 .이고 추가할 문자가 .이면 추가안함. 나머지는 추가
        if result[-1] == "." and c == ".":
            pass
        else:
            result += c
    return result


# 4. 마침표가 처음이나 끝에 위치한다면 제거
def step4(id):
    # 길이가 1이상인지 확인
    if len(id)>1:
        # 처음 확인
        if id[0] == ".":
            id = id[1:]
        # 마지막 확인
        if id[-1] == ".":
            id = id[:-1]
    else:
        # 길이가 1이하이고, 문자가 .이라면 빈 문자열 대입
        if id == ".":
            id = ""
    return id


# 5. 빈 문자열이라면 "a"리턴
def step5(id):
    if len(id) == 0:
        return "a"
    else:
        return id


# 6. 아이디가 16자 이상이면 15개만 남김
def step6(id):
    if len(id) >= 16:
        result = id[:15]
        # 15개 자른 문자중 마지막이 .이면 제거
        if result[-1] == ".":
            return result[:-1]
        else:
            return result
    else:
        return id


# 7. id가 2자 이하라면 마지막 문자를 길이 3이될때까지 붙혀줌.
def step7(id):
    if len(id) <= 2:
        last = id[-1]
        while len(id) < 3:
            id += last
    return id


def solution(new_id):
    id = step1(new_id)
    id = step2(id)
    id = step3(id)
    id = step4(id)
    id = step5(id)
    id = step6(id)
    id = step7(id)
    return id