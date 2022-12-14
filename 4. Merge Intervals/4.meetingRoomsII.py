# https://leetcode.com/problems/meeting-rooms-ii/

# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

# Heap Implementation:
from heapq import *


def meetingRooms(intervals):
    minHeap = []
    intervals.sort(key=lambda x: x[0])
    heappush(minHeap, intervals[0][1])
    for i in intervals[1:]:
        if minHeap[0] <= i[0]:
            heappop(minHeap)
        heappush(minHeap, i[1])
    return len(minHeap)


# Pointer based Implementation
def meetingRoomsI(intervals):
    meetingRooms = 0
    start_timings = sorted([i[0] for i in intervals])
    end_timings = sorted([i[1] for i in intervals])
    start, end = 0, 0
    while start < len(intervals):
        if start_timings[start] >= end_timings[end]:
            meetingRooms -= 1
            end += 1
        meetingRooms += 1
        start += 1
    return meetingRooms


if __name__ == "__main__":
    intervals = [[7, 10], [2, 4]]
    print(meetingRooms(intervals))
