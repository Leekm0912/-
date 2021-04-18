import collections


def solution(priorities, location):
    deque = collections.deque()
    queue = []
    # (index, value)꼴로 매핑하여 deque에 저장
    for i, v in enumerate(priorities):
        # 마지막에 위치를 조회하기 위해 저장해놓음.
        if i == location: remember = (v, i)
        deque.append((v, i))

    # deque 순회.
    while deque:
        # 요소를 대기목록에서 가져옴
        temp = deque.popleft()
        # 남은 대기목록이 없거나,
        # 우선순위가 높은항목이 deque안에 있다면.
        if deque and max(deque)[0] > temp[0]:
            # 맨 뒤로 보냄
            deque.append(temp)
        else:
            # 복사해줌(queue에 넣음.)
            queue.append(temp)

    # list의 인덱스 이므로 +1 해줌
    return queue.index(remember) + 1
