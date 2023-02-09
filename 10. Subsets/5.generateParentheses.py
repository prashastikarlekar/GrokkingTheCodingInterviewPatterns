# https://leetcode.com/problems/generate-parentheses/
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

from collections import deque


class Parenthesis:
    def __init__(self, str, openCount, closeCount):
        self.str = str
        self.openCount = openCount
        self.closeCount = closeCount


def generateParenthesis(N):
    result = []
    queue = deque()
    queue.append(Parenthesis("", 0, 0))
    while queue:
        current = queue.popleft()
        if current.openCount == N and current.closeCount == N:
            result.append(current.str)
        if current.openCount < N:
            queue.append(Parenthesis(
                current.str+"(", current.openCount+1, current.closeCount))
        if current.openCount > current.closeCount:
            queue.append(Parenthesis(current.str+")",
                         current.openCount, current.closeCount+1))
    return result


if __name__ == "__main__":
    print(generateParenthesis(3))
