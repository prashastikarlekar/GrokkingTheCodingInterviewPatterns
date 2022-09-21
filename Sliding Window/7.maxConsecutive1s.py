# https://leetcode.com/problems/max-consecutive-ones-iii/

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.


def maxOnes(nums, k):
    max_ones, max_length=0,0
    start,end=0,0
    while end<len(nums):
        if nums[end]==1: max_ones+=1
        end+=1
        countZeroes = end-start-max_ones
        if countZeroes > k:
            if nums[start]==1: max_ones-=1
            start+=1
        max_length=max(max_length,end-start)
    return max_length

        


if __name__ == "__main__":
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    print(maxOnes(nums, k))
