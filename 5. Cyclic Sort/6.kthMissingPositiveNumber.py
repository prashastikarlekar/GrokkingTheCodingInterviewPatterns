# https://leetcode.com/problems/kth-missing-positive-number/

# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
# Return the kth positive integer that is missing from this array.

def kthMissing(nums, k):
    i = 0
    missingNums = []
    while i < len(nums):
        j = nums[i]-1
        if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i+1:
            missingNums.append(i+1)
        if len(missingNums) == k:
            return missingNums[k-1]

    if len(missingNums) > 0:
        highestNotFound = missingNums[-1]
    else:
        highestNotFound = nums[-1]+1
        missingNums.append(highestNotFound)
    counter = len(missingNums)

    while counter < k:
        if highestNotFound+1 not in nums:
            missingNums.append(highestNotFound+1)
            counter += 1
        highestNotFound += 1

    return missingNums[k-1]


if __name__ == "__main__":
    # nums = [2, 3, 4, 7, 11]
    # k = 5
    # nums = [1, 2, 3, 4]
    # k = 2
    nums = [5, 6, 7, 8, 9]
    k = 9
    print(kthMissing(nums, k))
