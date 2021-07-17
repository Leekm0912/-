import collections


class MyHashMapWithChaining:
    # 내부에서 사용할 연결리스트.
    # defaultdict 사용위해 key와 value에 초기값을 줌.
    class ListNode:
        def __init__(self, key: int = None, value=None):
            self.key = key
            self.value = value
            self.next = None

    # 초기화
    def __init__(self, size: int = 1000):
        self.size = size
        self.table = collections.defaultdict(self.ListNode)

    # 키, 값을 해시맵에 삽입. 이미 존재하는 키라면 업데이트.
    def put(self, key: int, value):
        index = key % self.size
        # 인덱스에 노드가 없다면 삽입 후 종료.
        if self.table[index].value is None:
            self.table[index] = self.ListNode(key, value)
            return

        # 인덱스에 노드가 있을경우 연결리스트 처리. (update)
        p = self.table[index]
        while p:
            # 순회 중간에 일치하는 키를 발견하면 값을 업데이트 시키고 리턴.
            if p.key == key:
                p.value = value
                return
            # 다음노드가 없다면 멈추고 다음작업 실행.
            if p.next is None:
                break
            p = p.next
        # 순회가 끝나고도 작업처리가 안됐다면 연결리스트 맨 마지막에 추가.
        p.next = self.ListNode(key, value)

    # 키에 해당하는 값을 조회. 키가 존재하지 않으면 -1 리턴.
    def get(self, key: int):
        index = key % self.size
        # 존재하지 않는 키라면 -1 리턴
        if self.table[index].value is None:
            return -1

        # 노드가 존재하면 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    # 키에 해당하는 키, 값을 해시맵에서 삭제.
    def remove(self, key: int):
        index = key % self.size
        # 일치하는 키 없으면 바로 리턴.
        if self.table[index].value is None:
            return

        p = self.table[index]
        # 인덱스의 첫번째 노드일경우.
        if p.key == key:
            # 다음 노드가 없으면 빈 ListNode를 생성해줌. (put, get에서의 에러 방지.)
            if p.next is None:
                self.table[index] = self.ListNode()
                return
            # 다음 노드가 있다면 다음 노드를 테이블에 바로 연결.
            else:
                self.table[index] = p.next

        # 연결리스트 노드 삭제.
        prev = p
        while p:
            # 이전 노드에 현재 노드의 다음노드를 바로 연결시켜 현재 노드의 연결을 끊음.
            if p.key == key:
                prev.next = p.next
                return
            # 현재 노드를 이전으로 기억한 후 다음 노드로 이동.
            prev = p
            p = p.next

    def printTable(self):
        print("========printTable========")
        for t in self.table:
            p = self.table[t]
            while p:
                if p.value:
                    print("key:", p.key, "value:", p.value)
                if p.next:
                    print("연결리스트 연결", p.key, "to", p.next.key)
                p = p.next
        print("==========================")


if __name__ == "__main__":
    h = MyHashMapWithChaining(3)
    h.put(1, 1)
    h.put(2, 2)
    print(h.get(1))  # 1
    print(h.get(3))  # -1
    h.put(2, 1)
    print(h.get(2))  # 1
    h.remove(2)
    print(h.get(2))  # -1
    h.remove(4)
    h.put(3, 3)
    h.put(4, 4)
    h.put(5, 5)
    h.put(6, 6)
    h.put(7, 7)
    h.put(8, 8)
    h.put(9, 9)
    h.printTable()
    print(h.get(9))
