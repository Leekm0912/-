import collections


def solution(data: list) -> list:
    # 기본값으로 리스트를 생성하는 딕셔너리 객체 생성
    ddict = collections.defaultdict(list)
    for word in data:
        # key로 정렬된 word를 이용. <- 애너그램 확인
        # defaultdict에 의해 자동으로 생성된 리스트에 word를 append.
        ddict["".join(sorted(word))].append(word)
    # 딕셔너리의 value값만 추출해서 리스트로 변환 후 리턴
    return list(ddict.values())


print(solution(["eat", "tea", "tan", "ate", "nat", "bat"]))
