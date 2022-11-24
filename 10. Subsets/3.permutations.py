# https://leetcode.com/problems/permutations/

# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
from collections import deque


def permute(nums):
    numLength = len(nums)
    result = []
    permutations = deque()
    permutations.append([])
    for current in nums:
        n = len(permutations)
        for _ in range(n):
            oldPermutation = permutations.popleft()
            for j in range(len(oldPermutation)+1):
                newPermutation = list(oldPermutation)
                newPermutation.insert(j, current)
                if len(newPermutation) == numLength:
                    result.append(newPermutation)
                else:
                    permutations.append(newPermutation)
    return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(permute(nums))
