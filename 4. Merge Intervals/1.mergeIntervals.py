# https://leetcode.com/problems/merge-intervals/

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the
# intervals in the input.

def mergeIntervals(intervals):
    if len(intervals) < 2:
        return intervals
    result = []
    intervals.sort(key=lambda x: x[0])
    start = intervals[0][0]
    end = intervals[0][1]
    for i in range(1, len(intervals)):
        if end >= intervals[i][0]:
            end = max(end, intervals[i][1])
        else:
            result.append([start, end])
            start = intervals[i][0]
            end = intervals[i][1]
    result.append([start, end])
    return result


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(mergeIntervals(intervals))
