# https://leetcode.com/problems/3sum-closest/

# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers. You may assume that each input would have exactly one solution.

def threeSumClosest(nums, target):
    closest = float("inf")
    for i in range(len(nums)):
        low, high = i+1, len(nums)-1
        while low < high:
            sum = nums[i]+nums[low]+nums[high]
            if abs(target-nums[i]) < abs(closest):
                closest = target-nums[i]
            if sum < target:
                low += 1
            elif sum > target:
                high -= 1
        if closest == 0:
            break
    return target - closest


if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    target = 1
    print(threeSumClosest(nums, target))
