# Dutch National Flag Problem
# https://leetcode.com/problems/sort-colors/

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors
# in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

def sortColors(nums):
    low, current,  high = 0, 0, len(nums)-1
    while (current <= high):
        if nums[current] == 0:
            nums[low], nums[current] = nums[current], nums[low]
            low += 1
            current += 1
        elif nums[current] == 2:
            nums[current], nums[high] = nums[high], nums[current]
            high -= 1
        else:
            current += 1


if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    print(sortColors(nums))
