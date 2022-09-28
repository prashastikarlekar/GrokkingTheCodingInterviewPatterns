# https://leetcode.com/problems/squares-of-a-sorted-array/

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

def squareArray(nums):
    result = [None]*len(nums)
    left, right = 0, len(nums)-1
    for i in range(len(nums)-1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            square = nums[left]
            left += 1
        else:
            square = nums[right]
            right -= 1
        result[i] = square ** 2
    return result


if __name__ == "__main__":
    nums = [-7, -3, 2, 3, 11]
    print(squareArray(nums))
