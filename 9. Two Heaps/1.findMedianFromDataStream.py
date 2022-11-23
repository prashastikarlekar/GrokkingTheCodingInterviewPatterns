# https://leetcode.com/problems/find-median-from-data-stream/

# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

from heapq import *


class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

    # we want to keep equal elements in both heaps, but if there are odd elements, max heap should contain that one extra element so that we return median from it
        # maxheap has 2 or more extra elements than minheap, so we insert max element from maxheap into minheap
        if len(self.maxHeap) > len(self.minHeap)+1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (self.minHeap[0] + (-self.maxHeap[0]))/2.0
        return -self.maxHeap[0]/1.0


# Algorithm:

# 1. addNum(num):
#     1. check if maxHeap is empty OR num is smaller than the top element of maxHeap, which means it belongs in maxHeap
#     2. if not, insert it in minHeap
#     3. we wish to keep one extra element in the maxHeap in case of odd number of elements. To ensure both heaps have either
# equal elements or maxHeap has 1 more element than minHeap
#      If maxHeap has more than 1 extra element than minHeap, we push the top element of maxHeap in minHeap
#      If minHeap has more elements than maxHeap, we push smallest element from minHeap in maxHeap

# 2. findMedian:
#     1. if both the heaps have equal number of elements, we return median of top element of maxHeap and top element of minHeap, which give us the middle elements of stream
#     2. if lengths are unequal, that means maxHeap has one extra element, which gives us the middle of the stream and we return it.

# With operations regarding maxHeap, we put a (-) sign, because by deafult in python, heapq module has a minHeap and to use it as a maxHeap we put a - sign with
# operations concerning maxHeap.
# Note that we can only use - with operations, not with while referancing maxHeap like self.maxHeap, but with (-self.maxHeap[0])
#  Like on line 30 where length of minHeap is > length of maxHeap, we wish to push the minimum element from minHeap to maxHeap. Here we dont put - with self.maxHeap, but
#  instead we put it with -heappop(self.minHeap)
