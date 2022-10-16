# https://leetcode.com/problems/diameter-of-binary-tree/

# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def height(root):
    if not root:
        return -1
    return max(height(root.left), height(root.right))+1


def diameter(root):
    if not root:
        return 0
    factor1 = max(diameter(root.left), diameter(root.right))
    factor2 = height(root.left) + height(root.right)+2
    return max(factor1, factor2)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(-3)
    root.left.left = Node(3)
    root.left.left.left = Node(3)
    root.left.left.right = Node(-2)
    root.left.right = Node(2)
    root.left.right.right = Node(1)
    root.right.right = Node(11)
    print(diameter(root))
