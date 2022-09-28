# https://leetcode.com/problems/find-all-duplicates-in-an-array/

# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers
# that appears twice.
# You must write an algorithm that runs in O(n) time and uses only constant extra space.

def findDuplicates(nums):
    result = []
    i = 0
    while i < len(nums):
        j = nums[i]-1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(len(nums)):
        if nums[i] != i+1:
            result.append(nums[i])
    return result


if __name__ == "__main__":
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(findDuplicates(nums))
