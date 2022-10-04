from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def levelOrderSuccessor(root, node):
    if not root:
        return None
    queue = deque([root])
    while queue:
        levelLength = len(queue)
        for _ in range(levelLength):
            currentNode = queue.popleft()
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
            if currentNode.val == node.val:
                if queue:
                    return queue.popleft().val
                else:
                    return None
    return None


if __name__ == "__main__":
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)
    node = root.right.left
    print(levelOrderSuccessor(root, node))
