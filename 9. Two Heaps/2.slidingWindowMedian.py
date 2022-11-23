# https://leetcode.com/problems/sliding-window-median/

# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

# For examples, if arr = [2,3,4], the median is 3.
# For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
# You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.
from heapq import *
import heapq


class SlidingWindow:
    def __init__(self):
        self.max_heap, self.min_heap = [], []

    def find_median(self, nums, k):
        result = [0.0 for i in range(len(nums)-k + 1)]
        for i in range(len(nums)):
            if not self.max_heap or nums[i] < -self.max_heap[0]:
                heappush(self.max_heap, -nums[i])
            else:
                heappush(self.min_heap, nums[i])
            self.rebalance_heaps()

            if i-k+1 >= 0:
                if len(self.max_heap) == len(self.min_heap):
                    result[i-k+1] = (-self.max_heap[0] + self.min_heap[0])/2.0
                else:
                    result[i-k+1] = -self.max_heap[0]/1.0

                elementToBeRemoved = nums[i-k+1]
                if elementToBeRemoved <= -self.max_heap[0]:
                    self.remove(self.max_heap, -elementToBeRemoved)
                else:
                    self.remove(self.min_heap, elementToBeRemoved)
                self.rebalance_heaps()
        return result

    def remove(self, heap, element):
        index = heap.index(element)
        heap[index] = heap[-1]
        del heap[-1]
        if index < len(heap):
            heapq._siftup(heap, index)
            heapq._siftdown(heap, 0, index)

    def rebalance_heaps(self):
        if len(self.max_heap) > len(self.min_heap)+1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))


if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    slidingWindow = SlidingWindow()
    print(slidingWindow.find_median(nums, k))
