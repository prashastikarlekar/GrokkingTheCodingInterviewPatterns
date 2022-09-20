# https://leetcode.com/problems/maximum-subarray/

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.

def maximumSubarray(nums):
    current_sum, largest_sum = nums[0], nums[0]
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum+nums[i])
        largest_sum = max(current_sum, largest_sum)
    return largest_sum


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maximumSubarray(nums))
