from collections import deque

import CheckTime


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


@CheckTime.CheckTime
def solution(tree):
    queue = deque([tree])
    answer = 0

    while queue:
        answer += 1
        for _ in range(len(queue)):
            current_root = queue.popleft()

            if current_root.left:
                queue.append(current_root.left)
            if current_root.right:
                queue.append(current_root.right)
    return answer


if __name__ == "__main__":
    TreeNode(3,TreeNode(9),TreeNode(20))
    solution([3, 9, 20, None, None, 15, 7])
