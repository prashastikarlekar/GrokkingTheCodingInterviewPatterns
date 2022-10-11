# https://leetcode.com/problems/path-sum-ii/

# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be
# returned as a list of the node values, not node references.
# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def recursivePathSum(root, sum, currPath, allPaths):
    if root is None:
        return
    currPath.append(root.val)
    if root.val == sum and root.left is None and root.right is None:
        print(currPath)
        allPaths.append(list(currPath))
    else:
        recursivePathSum(root.left, sum-root.val, currPath, allPaths)
        recursivePathSum(root.right, sum-root.val, currPath, allPaths)
    del currPath[-1]


def pathSum(root, targetSum):
    allPaths = []
    recursivePathSum(root, targetSum, [], allPaths)
    return allPaths


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(4)
    root.right = Node(8)
    root.left.left = Node(11)
    root.right.left = Node(13)
    root.right.right = Node(4)
    root.left.left.left = Node(7)
    root.left.left.right = Node(2)
    root.right.right.left = Node(5)
    root.right.right.right = Node(1)
    print(pathSum(root, 22))
