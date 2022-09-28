# https://leetcode.com/problems/4sum/

# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target

def fourSum(nums, target):
    def kSum(nums, target, k):  # generalized solution for any sum problem
        result = []
        if not nums:
            return result
        average = target//k
        if average < nums[0] or nums[-1] < average:
            return result
        if k == 2:
            return twoSum(nums, target)

        for i in range(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                for subset in kSum(nums[i+1:], target-nums[i], k-1):
                    result.append([nums[i]] + subset)
        return result

    def twoSum(nums, target):
        low, high = 0, len(nums)-1
        result = []
        while low < high:
            sum = nums[low]+nums[high]
            # is the current element same as before, skip it
            if sum < target or (low > 0 and nums[low-1] == nums[low]):
                low += 1
            elif sum > target or (high < len(nums)-1 and nums[high] == nums[high+1]):
                high -= 1
            else:
                result.append([nums[low], nums[high]])
                low += 1
                high -= 1

        return result

    nums.sort()
    return kSum(nums, target, 4)


if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(fourSum(nums, target))
