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
        print("====================")

    @staticmethod
    @CheckTime.CheckTime
    def pareSwapByLoop(head: ListNode) -> ListNode:
        # 임시 저장
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            # a, b, c ...라고 할때 b의 주소를 기억
            temp = head.next
            # a의 다음을 b의 다음인 c로
            head.next = temp.next
            # b의 다음을 a로
            temp.next = head
            # 임시 저장소의 다음을 b로
            prev.next = temp

            # 다음 작업을 위해 이동
            # a의 다음인 c로 이동
            head = head.next
            # 임시저장소의 다음(b)의 다음(a)로.
            prev = prev.next.next
            # 이렇게 되면 각각 a, c를 가르키고 있으므로 다음 작업 수행 가능.
        # 수행이 끝난 후 임시저장소의 다음(b)를 리턴
        return root.next

    @staticmethod
    @CheckTime.CheckTime
    def pareSwapByRec(head: ListNode) -> ListNode:
        # 바꿀 값이 있을때 동작.
        if head and head.next:
            # a, b, c ... 일때 b의 주소를 저장
            temp = head.next
            # a의 다음을 호출(b의 다음인 c를 매개변수로.) 쭉쭉쭉가서 if문 안걸릴때까지.
            # d까지 있다고 하면 c까지 온다음(n-1) d를 넘겨주면 next가 없으니 if문 안걸려서 종료될꺼임.
            head.next = Solution.pareSwapByRec(temp.next)
            # b의 다음을 a로
            temp.next = head
            # b를 리턴
            return temp
        # if문 안걸리면 바로 리턴. (순환 종료)
        return head


if __name__ == "__main__":
    a = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    # Solution.printList(a)
    a = Solution.pareSwapByLoop(a)
    Solution.printList(a)
    Solution.printList(Solution.pareSwapByRec(a))
