# https://leetcode.com/problems/subarray-product-less-than-k/

# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is
#  strictly less than k.

def productLessThanK(nums, k):
    if k <= 1:
        return 0
    result = low = 0
    product = 1
    for i in range(len(nums)):
        product *= nums[i]
        if product >= k:
            product /= nums[low]
            low += 1
        result += i-low + 1
    return result


if __name__ == "__main__":
    nums = [10, 5, 2, 6]
    k = 100
    print(productLessThanK(nums, k))
