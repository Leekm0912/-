from codingTest import CheckTime


@CheckTime.CheckTime
def solution(data):
    answer = []
    stack = []
    for i in range(len(data)):
        if data[i][0] == "JFK":
            stack.append(data[i])
            answer.append(data[i][0])
            answer.append(data[i][1])
            data.remove(data[i])
            break

    while stack:
        now = stack.pop()
        save = []
        for i in range(len(data)):
            if data[i][0] == now[1]:
                save.append(data[i])

        save = sorted(save, key=lambda s: s[1], reverse=True)
        if save:
            stack.append(save[0])
            answer.append(save[0][1])
            data.remove(save[0])
    return answer


@CheckTime.CheckTime
def solution2(data):
    answer = []
    stack = []
    print(data)
    for i in range(len(data)):
        if data[i][0] == "ICN":
            if answer and answer[1]:
                if answer[1] > data[i][1]:
                    answer[0] = data[i][0]
                    answer[1] = data[i][1]
            else:
                answer.append(data[i][0])
                answer.append(data[i][1])
    temp = [answer[0], answer[1]]
    stack.append(temp)
    data.remove(temp)

    while stack:
        now = stack.pop()
        save = []
        for i in range(len(data)):
            if data[i][0] == now[1]:
                save.append(data[i])

        save.sort()
        print(save)
        if save:
            stack.append(save[0])
            answer.append(save[0][1])
            data.remove(save[0])
    return answer


@CheckTime.CheckTime
def solution3(ticket):
    # 입력값을 그래프로 만듬.
    graph = {}
    for i in range(len(ticket)):
        if ticket[i][0] not in graph:
            graph[ticket[i][0]] = [ticket[i][1]]
        else:
            graph[ticket[i][0]].append(ticket[i][1])

    for k in graph:
        # 그래프의 다음 노드를 이름순 정렬.
        graph[k].sort()

    # 스택을 이용해 반복적으로 dfs 구현.
    # 시작점을 ICN으로 설정.
    stack = ["ICN"]
    answer = []

    while stack:
        # 현재 스택의 값이 graph에 key로 존재하고, value가 비어있지 않으면(다음경로가 있으면) 반복.
        while stack[-1] in graph and graph[stack[-1]]:
            # 그래프의 다음 노드 목록에서 첫 값을 꺼내와 stack 추가.
            stack.append(graph[stack[-1]].pop(0))
        # 다음 목적지에 stack에 제일 최근에 들어온 값을 추가.
        answer.append(stack.pop())
    # 역순으로 되어있으므로, 뒤집어서 반환.
    return answer[::-1]


if __name__ == "__main__":
    # solution([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
    # solution2([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])
    solution3([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])
    solution3([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
