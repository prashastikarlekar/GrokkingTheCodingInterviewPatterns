# https://leetcode.com/problems/minimum-size-subarray-sum/

# Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the
#  sum is greater than or equal to target. If there is no such subarray, return 0 instead.

def minSubarray(nums, target):
    windowSum = 0
    start = 0
    minWindow = float("inf")
    for end in range(len(nums)):
        windowSum += nums[end]
        while windowSum >= target:
            minWindow = min(minWindow, end-start+1)
            windowSum -= nums[start]
            start += 1
    if minWindow == float("inf"):
        return 0
    return minWindow


if __name__ == "__main__":
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    print(minSubarray(nums, target))
