# https://leetcode.com/problems/missing-number/

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

def missingNumber(nums):
    i = 0
    while i < len(nums):
        j = nums[i]
        if nums[i] < len(nums) and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(len(nums)):
        if nums[i] != i:
            return i
    return len(nums)

    # for i in range(len(nums)):
    #     if nums[i] != i:
    #         return i
    # return len(nums)


if __name__ == "__main__":
    nums = [3, 0, 1]
    print(missingNumber(nums))
