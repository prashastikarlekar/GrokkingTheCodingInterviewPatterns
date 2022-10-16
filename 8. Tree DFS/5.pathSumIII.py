# https://leetcode.com/problems/path-sum-iii/

# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def recursivePathSum(root, targetSum, currPath):
    if not root:
        return 0
    currPath.append(root.val)
    pathCount, pathSum = 0, 0
    for i in range(len(currPath)-1, -1, -1):
        pathSum += currPath[i]
        if pathSum == targetSum:
            print(
                f"i is {i}, pathSum is {pathSum}, currPath is {currPath} currPath[i] is {currPath[i]}")
            pathCount += 1
    pathCount += recursivePathSum(root.left, targetSum, currPath)
    pathCount += recursivePathSum(root.right, targetSum, currPath)

    del currPath[-1]
    return pathCount


def pathSumIII(root, targetSum):
    return recursivePathSum(root, targetSum, [])


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
    print(pathSumIII(root, 8))
    # root = Node(5)
    # root.left = Node(4)
    # root.right = Node(8)
    # root.left.left = Node(11)
    # root.right.left = Node(13)
    # root.right.right = Node(4)
    # root.left.left.left = Node(7)
    # root.left.left.right = Node(2)
    # root.right.right.left = Node(5)
    # root.right.right.right = Node(1)
    # print(pathSumIII(root, 22))
