# https://leetcode.com/problems/find-right-interval/

# You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.
# The right interval for an interval i is an interval j such that startj >= endi and startj is minimized. Note that i may equal j.
# Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put -1 at index i.
from heapq import *


def findRightInterval(intervals):
    max_start_heap, max_end_heap = [], []
    result = [0 for i in range(len(intervals))]
    for endIndex in range(len(intervals)):
        heappush(max_end_heap, (-intervals[endIndex][1], endIndex))
        heappush(max_start_heap, (-intervals[endIndex][0], endIndex))
    for _ in range(len(intervals)):
        topEnd, endIndex = heappop(max_end_heap)
        result[endIndex] = -1
        if -max_start_heap[0][0] >= -topEnd:
            topStart, startIndex = heappop(max_start_heap)
            while max_start_heap and -max_start_heap[0][0] >= -topEnd:
                topStart, startIndex = heappop(max_start_heap)
            result[endIndex] = startIndex
            heappush(max_start_heap, (topStart, startIndex))

    return result


if __name__ == "__main__":
    print(findRightInterval([[3, 4], [2, 3], [1, 2]]))
