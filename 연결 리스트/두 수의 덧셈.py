from codingTest import CheckTime


class ListNode:
    def __init__(self, x, next_value=None):
        self.val = x
        self.next = next_value


class Solution:
    @staticmethod
    @CheckTime.CheckTime
    def addList(l1: ListNode, l2: ListNode) -> ListNode:
        l1_num = ""
        l2_num = ""
        node_a = l1
        node_b = l2

        while node_a:
            l1_num += str(node_a.val)
            node_a = node_a.next

        while node_b:
            l2_num += str(node_b.val)
            node_b = node_b.next

        l1_list = list(l1_num)
        l1_list.reverse()
        l1_val = "".join(l1_list)

        l2_list = list(l2_num)
        l2_list.reverse()
        l2_val = "".join(l2_list)

        result_str = str(int(l1_val) + int(l2_val))

        prev = None
        for s in result_str:
            node = ListNode(s)
            node.next = prev
            prev = node
        return node

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
    a = ListNode(2, ListNode(4, ListNode(3)))
    b = ListNode(5, ListNode(6, ListNode(4)))
    Solution.printList(Solution.addList(a, b))
