# https://leetcode.com/problems/binary-search/
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then
# return its index. Otherwise, return -1.

def binarySearch(nums, key):
    start, end = 0, len(nums)-1
    isAscending = nums[start] < nums[end]
    while start <= end:
        mid = start + (end-start) // 2
        if key == nums[mid]:
            return mid
        if isAscending:
            if key < nums[mid]:
                end = mid-1
            else:
                start = mid+1
        else:
            if key < nums[mid]:
                start = mid+1
            else:
                end = mid-1
    return -1


if __name__ == "__main__":
    print(binarySearch([1, 2, 3, 4, 5, 6, 7], 5))
