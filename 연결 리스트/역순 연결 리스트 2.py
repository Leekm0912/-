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
    def soluion1(head: ListNode, m, n) -> ListNode:
        root = start = ListNode(None)
        root.next = head
        # start는 m보다 한칸 앞, end는 m만큼
        # start와 end값을 고정.
        for _ in range(m-1):
            start = start.next
        end = start.next
        
        # start는 가만히 놔두면서, end가 전진
        # start의 다음 노드를 계속 바꿔주는 식.
        for _ in range(n - m):
            # start의 다음노드 저장.
            temp = start.next
            # start의 다음 노드를 end의 다음 노드로 변경.
            start.next = end.next
            # end의 다음 노드를 end의 다음 다음 노드로 변경.
            end.next = end.next.next
            # start의 다음 다음노드를 저장해놨던 원래 start의 다음노드로 변경
            start.next.next = temp
        # 기억해놓은 root(None)의 다음 노드(head)를 리턴
        return root.next


if __name__ == "__main__":
    a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    a = Solution.soluion1(a, 2, 4)
    Solution.printList(a)
