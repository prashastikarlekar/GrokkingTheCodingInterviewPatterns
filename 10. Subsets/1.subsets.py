# https://leetcode.com/problems/subsets/

# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

def subsets(nums):
    subset = []
    subset.append([])
    for current in nums:  # for every element in nums, add this current element to every element in subset
        for i in range(len(subset)):
            set = list(subset[i])
            set.append(current)
            subset.append(set)
    return subset


if __name__ == "__main__":
    nums = [1, 5, 3]
    print(subsets(nums))
