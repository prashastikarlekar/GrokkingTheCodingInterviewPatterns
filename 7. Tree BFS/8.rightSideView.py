# https://leetcode.com/problems/binary-tree-right-side-view/

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def rightSideView(root):
    output = []
    if not root:
        return output
    queue = deque([root])
    while queue:
        levelLength = len(queue)
        while (levelLength):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if levelLength == 1:
                output.append(node.val)
            levelLength -= 1
    return output


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.right = Node(4)
    root.left.right = Node(5)
    print(rightSideView(root))
