def solution(progresses, speeds):
    answer = []
    map_list = []

    for i in range(len(progresses)):
        map_list.append([progresses[i], speeds[i]])
    while map_list:
        end = []
        for i, v in enumerate(map_list):
            map_list[i][0] += v[1]

        while map_list and map_list[0][0] >= 100:
            end.append(map_list[0])
            del map_list[0]

        if len(end) > 0:
            answer.append(len(end))

    return answer
