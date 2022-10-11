# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# You are given the root of a binary tree containing digits from 0 to 9 only. Each root-to-leaf path in the tree represents a number.
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def recursiveSumNodes(root,currPath,total):
    if not root:
        return 0
    currPath.append(root.val)
    if not root.left and not root.right:
        # print(currPath)
        j=''
        for i in currPath:
            # print(i)
            j+=str(i)
            # print(j)
            # print(total)
        total=int(j)
        
    else:
        left=recursiveSumNodes(root.left, currPath,total)
        right=recursiveSumNodes(root.right, currPath, total)
        total=left+right
    del currPath[-1]
    return total

def sumNodes(root):
    total=0
    return recursiveSumNodes(root,[],total)


if __name__=="__main__":
    root=Node(4)
    root.left=Node(9)
    root.right=Node(0)
    root.left.right=Node(1)
    root.left.left=Node(5)
    print(sumNodes(root))

 