import re
import collections


def solution(paragraph: str, banned: list) -> str:
    words = list()
    for word in paragraph.lower().split():
        # sub(패턴, 치환할문자, 문자열) : 문자열을 주면 정규표현식에 해당하는 문자를 지정한 문자로 치환.
        # ^ : not, \w : 단어 문자. [ ] : 문자열 전체를 대상으로 하는 의미인듯. 안붙이면 이상한 결과 나옴.
        # 즉 단어 문자가 아닌것들을 공백으로 치환.
        temp = re.sub(r"[^\w]", "", word)
        # 금지된 단어가 아니라면 저장.
        if temp not in banned:
            words.append(temp)
    
    # collections의 Counter를 이용해 빈도순으로 자동정렬
    counter = collections.Counter(words)
    # 가장 많이나온 하나를 리턴함
    return counter.most_common(1)[0][0]


print(solution("Bob hit a ball, the hit BALL flew far after it was hit", ["hit"]))
