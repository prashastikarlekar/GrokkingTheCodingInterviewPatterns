# https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def levelAverages(root):
    output = []
    if not root:
        return output
    queue = deque([root])
    while queue:
        levelLength = len(queue)
        levelSum = 0.0
        for _ in range(levelLength):
            node = queue.popleft()
            levelSum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        output.append(levelSum/levelLength)
    return output


if __name__ == "__main__":
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)
    print(levelAverages(root))
