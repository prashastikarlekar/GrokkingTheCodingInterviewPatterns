# https://leetcode.com/problems/employee-free-time/
# We are given a list schedule of employees, which represents the working time for each employee. Each employee has a list of non-overlapping Intervals, and these intervals
# are in sorted order. Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.
# Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1,
# schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.
from heapq import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def employeeFreeTime(schedule):
    freeTime = []
    minHeap = []
    for emp_index, emp_schedule in enumerate(schedule):
        heappush(minHeap, (emp_schedule[0].start, emp_index, 0))
    _, emp_index, event_index = minHeap[0]
    prev_end = schedule[emp_index][event_index].end

    while minHeap:
        start, emp_index, event_index = heappop(minHeap)
        if event_index < len(schedule[emp_index])-1:
            heappush(
                minHeap, (schedule[emp_index][event_index+1].start, emp_index, event_index+1))
        if prev_end < start:
            freeTime.append(Interval(start=prev_end, end=start))
        prev_end = max(prev_end, schedule[emp_index][event_index].end)
    return freeTime


if __name__ == "__main__":
    schedule = [[Interval(1, 2), Interval(5, 6)], [Interval(1, 3)]], [
        Interval(4, 10)]
    print(employeeFreeTime(schedule))
