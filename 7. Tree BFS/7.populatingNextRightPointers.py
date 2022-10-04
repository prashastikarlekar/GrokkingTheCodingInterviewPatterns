# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;}
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None


def populateRightPointers(root):
    if root is None:
        return None
    queue = deque([root])
    while queue:
        levelLength = len(queue)
        while levelLength:
            node = queue.popleft()
            if levelLength == 1:
                node.next = None
            else:
                node.next = queue[0]
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            levelLength -= 1
    return root


if __name__ == "__main__":
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)
    node = root.right.left
    print(populateRightPointers(root))
