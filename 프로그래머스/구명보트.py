def solution(people, limit):
    answer = 1
    now = 0
    count = 0
    # 내림차순 정렬
    people.sort(reverse=True)

    # 효율성 부분때문에 del등 쓰지않고 인덱스로 접근해야함.
    # 맨 앞사람 인덱스
    f = 0
    # 맨 뒷사람 인덱스
    l = len(people) - 1

    # 뒷사람 인덱스가 앞사람 인덱스보다 크거나 같을동안. (앞사람의 인덱스가 더 커지면 종료)
    while (f <= l):
        # 현재 무게와 i의 값을 더한것이 limit와 작거나 같고
        # 보트에 타고있는 사람이 2명 이하라면
        if (count < 2 and now + people[f] <= limit):
            # 보트에 같이 태움
            now += people[f]
            f += 1
            count += 1
        # 제일 가벼운사람 태울수 있는지 확인
        elif (count < 2 and now + people[l] <= limit):
            # 보트에 같이 태움
            now += people[l]
            l -= 1
            count += 1
        else:
            # 보트를 따로 태우고 보트 대수를 1 증가시킴.
            now = people[f]
            f += 1
            count = 1
            answer += 1

    return answer