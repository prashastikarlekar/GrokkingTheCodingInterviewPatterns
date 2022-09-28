# https://leetcode.com/problems/interval-list-intersections/

# You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is
# pairwise disjoint and in sorted order. Return the intersection of these two interval lists.
# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
# The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and
# [2, 4] is [2, 3].

def intervalIntersection(firstList, secondList):
    result = []
    start, end, i, j = 0, 1, 0, 0
    while i < len(firstList) and j < len(secondList):
        a_overlaps_b = firstList[i][start] >= secondList[j][start] and firstList[i][start] <= secondList[j][end]
        b_overlaps_a = secondList[j][start] >= firstList[i][start] and secondList[j][start] <= firstList[i][end]
        if a_overlaps_b or b_overlaps_a:
            result.append([max(firstList[i][start], secondList[j][start]), min(
                firstList[i][end], secondList[j][end])])
        if firstList[i][end] < secondList[j][end]:
            i += 1
        else:
            j += 1
    return result


if __name__ == "__main__":
    firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
    secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
    print(intervalIntersection(firstList, secondList))
