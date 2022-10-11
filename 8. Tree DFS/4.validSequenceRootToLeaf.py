# https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/description/

# Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string is a valid sequence in such binary tree.
# We get the given string from the concatenation of an array of integers arr and the concatenation of all values of the nodes along a path results in a sequence in the given
# binary tree.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def recursiveValidSequence(root, arr, currPath):
    if not root:
        return False
    currPath.append(root.val)
    if root.left is None and root.right is None:
        if currPath == arr:
            # del currPath[-1]
            return True
        del currPath[-1]

        return False
    else:
        flag = recursiveValidSequence(
            root.left, arr, currPath) or recursiveValidSequence(root.right, arr, currPath)
    print(currPath)
    del currPath[-1]
    return flag


def validSequence(root, arr):
    return recursiveValidSequence(root, arr, [])


if __name__ == "__main__":
    # root = Node(0)
    # root.left = Node(1)
    # root.right = Node(0)
    # root.left.left = Node(0)
    # root.left.left.right = Node(1)
    # root.left.right = Node(1)
    # root.left.right.left = Node(0)
    # root.left.right.right = Node(0)
    # root.right.left = Node(0)
    root = Node(8)
    root.right = Node(8)
    root.right.right = Node(9)
    root.right.right.left = Node(5)
    root.right.right.left.left = Node(7)
    root.right.right.left.right = Node(3)
    root.right.right.left.left.right = Node(8)
    root.right.right.left.right.left = Node(2)

    # arr = [0, 1, 0, 1]
    arr = [8, 8, 9, 5, 3, 2]
    print(validSequence(root, arr))
