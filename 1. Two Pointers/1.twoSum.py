# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def twoSum(nums, target):
    visited = {}  # keeps track of visited elements and their indexes
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in visited:
            return [i, visited[complement]]
        visited[nums[i]] = i
    return None


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))
