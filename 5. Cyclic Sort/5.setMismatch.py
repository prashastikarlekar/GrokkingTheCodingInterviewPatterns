# https://leetcode.com/problems/set-mismatch/

# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another
# number in the set, which results in repetition of one number and loss of another number.
# You are given an integer array nums representing the data status of this set after the error.
# Find the number that occurs twice and the number that is missing and return them in the form of an array.

def setMismatch(nums):
    start = 0
    while start < len(nums):
        i = nums[start]-1
        if nums[start] != nums[i]:
            nums[start], nums[i] = nums[i], nums[start]
        else:
            start += 1
    for i in range(len(nums)):
        if nums[i] != i+1:
            return [nums[i], i+1]


if __name__ == "__main__":
    nums = [1, 2, 2, 4]
    print(setMismatch(nums))
