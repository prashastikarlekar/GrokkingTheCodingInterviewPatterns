# https://leetcode.com/problems/subsets-ii/

# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

def subsetsII(nums):
    result = [[]]
    nums.sort()
    start, end = 0, 0
    for i in range(len(nums)):
        start = 0
        if i > 0 and nums[i] == nums[i-1]:
            start = end+1
        end = len(result)-1
        for j in range(start, end+1):
            set = list(result[j])
            set.append(nums[i])
            if set not in result:
                result.append(set)

    return result


if __name__ == "__main__":
    nums = [1, 2, 2]
    print(subsetsII(nums))
