# https://leetcode.com/problems/first-missing-positive/

# Given an unsorted integer array nums, return the smallest missing positive integer. You must implement an algorithm that runs in O(n) time and uses constant extra space.

def firstPositiveNumber(nums):
    i = 0
    while i < len(nums):
        j = nums[i]-1
        if j > len(nums):
            j = j - (len(nums)+1)
        if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(len(nums)):
        if nums[i] != i+1:
            return i+1
    return len(nums)+1


if __name__ == "__main__":
    # nums = [1, 2, 0]
    # nums = [3, 4, -1, 1]
    nums = [7, 8, 9, 11, 12]
    print(firstPositiveNumber(nums))
