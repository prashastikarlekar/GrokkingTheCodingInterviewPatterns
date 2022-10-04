# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then
#  right to left for the next level and alternate between).

from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def zigzagLevelOrder(root):
    output = []
    if not root:
        return output
    queue = deque([root])
    stack, level = [], 0
    while queue:
        levelLength = len(queue)
        currentLevel = []
        for _ in range(levelLength):
            node = queue.popleft()
            if level % 2 == 0:
                currentLevel.append(node.val)
            else:
                stack.append(node)
                if len(stack) == levelLength:
                    while stack:
                        currentLevel.append(stack.pop().val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        output.append(currentLevel)
        level += 1
    return output


if __name__ == "__main__":
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)
    print(zigzagLevelOrder(root))
