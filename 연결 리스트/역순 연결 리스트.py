class ListNode:
    def __init__(self, x, next_value=None):
        self.val = x
        self.next = next_value


class Solution:
    @staticmethod
    def reverseList(head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            # node가 null일때까지 찾음.
            if not node:
                # null이면 이전 노드를 리턴.
                return prev
            # node가 null이 아니면,
            # 현재 node가 가지고있는 다음 노드를 변수에 저장하고
            # 이전 노드를 현재 node의 next에 넣어줌.
            next_node, node.next = node.next, prev
            # 그 후 next_node (원래 next였던 노드), node(현재 노드)를 실행시켜줌
            return reverse(next_node, node)

        # 제일 첫 node를 인자로 주면서 작동시킴.
        return reverse(head)

    @staticmethod
    def reverseList2(li: ListNode) -> ListNode:
        node = li
        prev = None
        while node:
            # 다음 노드를 temp에 저장.
            temp = node.next
            # 이전 노드를 현재 노드의 다음노드로.
            node.next = prev
            # 이전 노드를 현재 노드로.
            prev = node
            # temp에 저장해놨던 다음노드를 현재 노드로.
            node = temp
        return prev

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


if __name__ == "__main__":
    a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    # Solution.printList(a)
    Solution.printList(Solution.reverseList(a))
    a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    Solution.printList(Solution.reverseList2(a))
