# https://leetcode.com/problems/path-sum/

# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
# A leaf is a node with no children.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def pathSum(root, targetSum, path=[]):
    if not root:
        return False
    if root.val == targetSum and root.left is None and root.right is None:
        path.append(root.val)
        return True
    return pathSum(root.left, targetSum-root.val) or pathSum(root.right, targetSum-root.val)


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(4)
    root.right = Node(8)
    root.left.left = Node(11)
    root.right.left = Node(13)
    root.right.right = Node(4)
    root.left.left.left = Node(7)
    root.left.left.right = Node(2)
    root.right.right.right = Node(1)
    print(pathSum(root, 21))
