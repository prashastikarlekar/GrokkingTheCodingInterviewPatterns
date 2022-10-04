# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Given a binary tree, find its minimum depth. The minimum depth is the number of nodes along the shortest path from the root
#  node down to the nearest leaf node. Note: A leaf is a node with no children.
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def minDepth(root):
    if not root:
        return 0
    queue = deque([root])
    minDepth = 0
    while queue:
        minDepth += 1
        levelLength = len(queue)
        for _ in range(levelLength):
            node = queue.popleft()
            if not node.left and not node.right:
                return minDepth
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return minDepth


if __name__ == "__main__":
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)
    print(minDepth(root))
