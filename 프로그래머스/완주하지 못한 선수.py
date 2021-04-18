def solution(participant, completion):
    # 정렬
    participant.sort()
    completion.sort()
    answer = ""

    # 비교 도중 틀린것이 있으면 탈락자.
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    # 끝까지 틀린게 없으면 마지막 사람이 탈락자.
    if answer == "":
        answer = participant[-1]

    return answer
