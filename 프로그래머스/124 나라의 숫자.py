def solution(n):
    answer = ''
    number = ["1", "2", "4"]
    temp = ""
    while n > 3:
        n, a = divmod(n-1, 3)

        temp += number[a]

    if n != 0:
        temp += number[n-1]

    for s in reversed(temp):
        answer += s
    return answer
