def missingNumber(nums):
    start = 0
    while start < len(nums):
        num = nums[start]
        # if the number is not equal to its index then swap
        if num < len(nums) and num != start:
            nums[start], nums[num] = nums[num], nums[start]
        else:
            start += 1
    for i in range(len(nums)):
        if nums[i] != i:
            return i
    return len(nums)


if __name__ == "__main__":
    nums = [3, 0, 1]
    print(missingNumber(nums))
