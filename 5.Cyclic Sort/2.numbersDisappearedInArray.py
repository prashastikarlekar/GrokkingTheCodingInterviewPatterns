# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

def findDisapperaredNumbers(nums):
    start = 0
    while start < len(nums):
        num = nums[start]
        if num < len(nums) and num != start:
            nums[start], nums[num] = nums[num], nums[start]
        else:
            start += 1
    return nums


if __name__ == "__main__":
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(findDisapperaredNumbers(nums))
