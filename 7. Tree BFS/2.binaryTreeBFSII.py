# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def levelOrder(root):
    output = []
    if not root:
        return output
    queue = deque([root])
    stack = []
    while queue:
        levelLength = len(queue)
        currentLevel = []
        for _ in range(levelLength):
            node = queue.popleft()
            currentLevel.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        stack.append(currentLevel)
    while stack:
        output.append(stack.pop())
    return output


if __name__ == "__main__":
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)
    print(levelOrder(root))
