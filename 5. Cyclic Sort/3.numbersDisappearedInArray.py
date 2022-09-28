# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

def findDisapperaredNumbers(nums):
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
            result.append(i+1)
    return result


if __name__ == "__main__":
    # nums = [4, 3, 2, 7, 8, 2, 3, 1]
    nums = [1, 1]
    print(findDisapperaredNumbers(nums))
