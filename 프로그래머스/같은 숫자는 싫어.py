def solution(arr):
    answer = []
    last = ""
    for i in arr:
        if last != i:
            answer.append(i)
        last = i
    return answer
