# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Since it is impossible to change the length of the array in some languages,
# you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates,
#  then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
# Return k after placing the final result in the first k slots of nums.
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

def removeDuplicates(nums):
    fixed = 0  # gives the number of elements in nums that have been fixed with given criteria
    for i in range(1, len(nums)):
        # both elements are not same, so move ahead and assign next to fixed element as the current element
        if nums[i] != nums[fixed]:
            fixed += 1
            nums[fixed] = nums[i]
    return fixed + 1


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(removeDuplicates(nums))
