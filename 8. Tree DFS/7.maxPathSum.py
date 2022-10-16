# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most
#  once. Note that the path does not need to pass through the root. The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any non-empty path.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def recursiveMaxPathSum(self, root):
        if not root:
            return 0
        maxLeftSum = self.recursiveMaxPathSum(root.left)
        maxRightSum = self.recursiveMaxPathSum(root.right)
        maxLeftSum = max(maxLeftSum, 0)
        maxRightSum = max(maxRightSum, 0)

        localMax = maxLeftSum+maxRightSum+root.val
        self.globalMax = max(self.globalMax, localMax)
        return max(maxLeftSum, maxRightSum)+root.val

    def maxPathSum(self, root):
        self.globalMax = float("-inf")
        self.recursiveMaxPathSum(root)
        return self.globalMax


if __name__ == "__main__":
    solution = Solution()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    print(solution.maxPathSum(root))
