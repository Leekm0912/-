from codingTest import CheckTime


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
    @CheckTime.CheckTime
    def soluion1(head: ListNode) -> ListNode:
        # 홀수와 짝수 리스트
        odd_root = odd = ListNode(None)
        even_root = even = ListNode(None)

        while head:
            # 짝수
            if head.val % 2 == 0:
                # 홀수 연결리스트의 다음노드에 현재 리스트를 지정
                even.next = head
                # 한칸 이동
                even = even.next
            # 홀수
            else:
                # 홀수 연결리스트의 다음노드에 현재 리스트를 지정
                odd.next = head
                # 한칸 이동
                odd = odd.next
            # 다음 리스트 이동
            head = head.next
            # 오류 방지 초기화 작업
            odd.next = None
            even.next = None
        # 홀수 다음 짝수 리스트가 오도록 연결
        odd.next = even_root.next
        # 홀수 연결 리스트의 다음(시작부분) 을 리턴
        return odd_root.next


if __name__ == "__main__":
    a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    a = Solution.soluion1(a)
    Solution.printList(a)
