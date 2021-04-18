def solution(bridge_length, weight, truck_weights):
    # truck_weights[::-1] 이유는 효율성때문이다.
    # truck_weights를 거꾸로 뒤집어주지 않으면 truck_weights.pop()이 아닌 truck_weights.pop(0)을 해야하는데,
    # 이렇게 되면 첫 번째 원소를 빼고 그 뒤에 원소들을 한칸씩 앞으로 모두 땡겨줘야하기 때문에
    # O(n)만큼 걸린다. 즉 비효율적이다.

    # 따라서 truck_weights를 거꾸로 뒤집어 truck_weights.pop() 으로 해주면
    # 가장 뒤에 원소만 하나씩 빠지기 때문에 O(1)에 할 수 있다.
    truck_weights = truck_weights[::-1]

    # 트럭의 대수
    n = len(truck_weights)
    # 각 트럭이 다리에 오르는 순간부터 얼마의 시간이 흘렀는지를 나타내는 리스트
    passing_weight = [0] * n
    # 지나간 트럭
    passed = []
    # 지나가는중인 트럭
    passing = []

    # 가장 선두에서 지나는 트럭의 index :: bridge_length만큼 다리위에 있었는지 확인하기 위함
    i = 0
    # 가장 최근 다리에 올라간 트럭의 index :: passing_weight에 indexing하기 위함
    j = -1

    # 트럭의 대수와 지나간 대수가 같아지면 종료.
    while len(passed) < n:
        # 1. 지나갈 트럭이 아직 남았고,
        # 2. 다리위의 트럭과 지나가려는 트럭의 무게의 합이 무게제한보다 작거나 같다면
        if len(truck_weights) > 0 and sum(passing) + truck_weights[-1] <= weight:
            # 다리위에 올림.
            passing.append(truck_weights.pop())
            # 가장 최근에 다리위에 올라간 트럭을 나타내기 위해 인덱스 조절
            j += 1

        # 다리에 올라간 트럭들의 시간을 모두 +1 해줌.
        # 지나가도 늘어남 <- 첫차를 이용해 시간계산 가능.
        for z in range(j + 1):
            passing_weight[z] += 1

        # 다리위에서 있던(움직인) 시간과 다리의 길이가 같다면
        if passing_weight[i] == bridge_length:
            # 지나간 트럭에 추가.
            passed.append(passing[0])
            # 추가했으니 지워줌. 슬라이싱 이용
            passing = passing[1:]
            # 지나갔으니 선두 트럭 인덱스 조정.
            i += 1

    # 제일 첫차의 시간과 마지막 트럭이 빠져나오는 시간을 더해줌 (+1)
    return passing_weight[0] + 1