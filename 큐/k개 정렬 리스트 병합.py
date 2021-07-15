# k개의 정렬된 리스트를 1개의 정렬된 리스트로 병합하라.
import heapq
from typing import List

from CheckTime import CheckTime


class ListNode:
    def __init__(self, x, next_value=None):
        self.val = x
        self.next = next_value


class Solution:
    @staticmethod
    def printList(li, text=None):
        if text:
            print("==========" + text + "==========")
        else:
            print("====================")
        while li and li.val:
            print(li.val)
            li = li.next
        # 정상적이라면 None 출력
        print(li)
        print("====================")

    @staticmethod
    @CheckTime
    def solution1(data: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []

        # 각 연결리스트의 루트를 힙에 저장.
        for i in range(len(data)):
            if data[i]:
                # 저장할때 값, 루트 인덱스 번호, 객체 순 저장.
                heapq.heappush(heap, (data[i].val, i, data[i]))

        # 힙 추출 이후 다음 노드는 다시 저장.
        # 가장 작은 노드를 뽑은 후 뽑은 노드를 result에 연결 하고 다음 노드를 다시 힙에 넣는걸 반복.
        while heap:
            # 값이 가장 작은 노드 하나를 뺌.
            node = heapq.heappop(heap)
            # 노드의 루트 인덱스 번호 불러옴(중복 방지용)
            idx = node[1]
            # 결과에 해당 객체를 연결
            result.next = node[2]
            # 다음 노드로 이동
            result = result.next
            # 이동 후 다음 노드가 있다면
            if result.next:
                # 해당 노드를 힙에 저장.
                heapq.heappush(heap, (result.next.val, idx, result.next))
        return root.next


if __name__ == "__main__":
    a = [
        ListNode(1, ListNode(4, ListNode(5))),
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(2, ListNode(6))
    ]
    a = Solution.solution1(a)
    Solution.printList(a)
