# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

# Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will
#  be sorted in ascending order.
# Return the shortest such subarray and output its length.

# Followed solution Approach#5 on leetcode

def findShortestSubarray(nums):
    # denote min and max value in unsorted array
    minValue, maxValue = float("inf"), float("-inf")
    flag = False
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            flag = True
        if flag:
            minValue = min(minValue, nums[i])
    flag = False
    for i in range(len(nums)-2, -1, -1):
        if nums[i] > nums[i+1]:
            flag = True
        if flag:
            maxValue = max(maxValue, nums[i])
    low, high = 0, 0
    for i in range(len(nums)):
        if nums[i] > minValue:  # finding the element just greater than min value of unsorted array
            low = i
            break
    for i in range(len(nums)-1, -1, -1):
        if nums[i] < maxValue:
            high = i
            break
    return 0 if high-low <= 0 else high-low+1


if __name__ == "__main__":
    nums = [2, 6, 4, 8, 10, 9, 15]
    print(findShortestSubarray(nums))
