
def threeSumClosest(nums, target):
    answer = 0
    nums.sort()
    for i in range(len(nums)):
        low, high = i+1, len(nums)-1
        while low < high:
            sum = nums[i]+nums[low]+nums[high]
            if sum < target:
                # once we find current sum < target, all elements between left and right will also give sum < target
                answer += high - low
                low += 1
            else:
                high -= 1
    return answer


if __name__ == "__main__":
    nums = [-2, 0, 1, 3]
    target = 2
    print(threeSumClosest(nums, target))
