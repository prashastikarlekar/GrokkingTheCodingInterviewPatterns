# https://leetcode.com/problems/ipo/

# Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its
# capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its
# total capital after finishing at most k distinct projects.
# You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.
# Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.
# Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.
# The answer is guaranteed to fit in a 32-bit signed integer.
from heapq import *


def findMaximizedCapital(k, w, profits, capital):
    max_profit_heap, min_capital_heap = [], []
    availableCapital = w
    for i in range(len(profits)):
        heappush(min_capital_heap, (capital[i], i))

    for _ in range(k):
        while min_capital_heap and min_capital_heap[0][0] <= availableCapital:
            capital, i = heappop(min_capital_heap)
            heappush(max_profit_heap, (-profits[i], i))
        if not max_profit_heap:
            break
        availableCapital += -heappop(max_profit_heap)[0]

    return availableCapital

    return w


if __name__ == "__main__":
    print(findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]))
