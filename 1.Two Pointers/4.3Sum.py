# https://leetcode.com/problems/3sum/

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and
# nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

def threeSum(nums):
    answer = []
    nums.sort()
    for i in range(len(nums)):
        # if current element is > 0 , there is no way further elemnts will sum up to 0.
        if nums[i] > 0:
            break
        # if previous element is same as current, skip it
        if i == 0 or nums[i-1] != nums[i]:
            twoSumHelper(nums, i, answer)
    return answer


def twoSumHelper(nums, i, answer):
    low, high = i+1, len(nums)-1
    while low < high:
        sum = nums[i]+nums[low]+nums[high]
        if sum < 0:
            low += 1
        elif sum > 0:
            high -= 1
        else:
            answer.append([nums[i], nums[low], nums[high]])
            low += 1
            high -= 1
            # if next element is same as previous element, skip it
            while low < high and nums[low-1] == nums[low]:
                low += 1


if __name__ == "__main__":
    nums = nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))
