# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, group, next_value=None):
        self.val = x
        self.next = next_value
        self.group = group


class Solution:
    @staticmethod
    def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            print("l1 :", l1.val, l1.group, "l2 :", l2.val, l2.group)
        # (l1 값이 없거나), (l2 값이 있는데, l1의 값이 더 크다면)
        if (not l1) or (l2 and l1.val > l2.val):
            # l1과 l2중 작은값을 왼쪽에 오게함.
            l1, l2 = l2, l1
        # l1(작은값)이 있으면 (null이 아니라면)
        if l1:
            # 작은값의 다음 노드를 호출후 결과를 연결
            l1.next = Solution.mergeTwoLists(l1.next, l2)
        # 작은값을 리턴
        return l1

    @staticmethod
    def printList(li, text=None):
        if text:
            print("==========" + text + "==========")
        else:
            print("====================")
        while li and li.val:
            print(li.val, li.group)
            li = li.next


if __name__ == "__main__":
    a = ListNode(1, "a", ListNode(2, "a", ListNode(4, "a")))
    Solution.printList(a, "a")
    b = ListNode(1, "b", ListNode(3, "b", ListNode(4, "b")))
    Solution.printList(b, "b")
    Solution.printList(Solution.mergeTwoLists(a, b))
