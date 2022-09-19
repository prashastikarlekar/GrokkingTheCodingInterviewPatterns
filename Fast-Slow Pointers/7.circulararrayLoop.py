# https://leetcode.com/problems/circular-array-loop/

# You are playing a game involving a circular array of non-zero integers nums. Each nums[i] denotes the number of indices forward/backward you must move if you are located at
# index i:
# If nums[i] is positive, move nums[i] steps forward, and
# If nums[i] is negative, move nums[i] steps backward.
# Since the array is circular, you may assume that moving forward from the last element puts you on the first element, and moving backwards from the first element puts you on
# the last element.
# A cycle in the array consists of a sequence of indices seq of length k where:
# Following the movement rules above results in the repeating index sequence seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
# Every nums[seq[j]] is either all positive or all negative.
# k > 1
# Return true if there is a cycle in nums, or false otherwise.

def circularArray(nums):
    for i in range(len(nums)):
        forward = nums[i] >= 0
        slow, fast = i, i
        while True:
            slow = getIndex(nums, slow, forward)  # move slow by one step
            fast = getIndex(nums, fast, forward)  # move fast fast by one step
            if fast != -1:  # check if fast is already not -1, if not move fast by another step
                fast = getIndex(nums, fast, forward)
            if slow == -1 or fast == -1 or slow == fast:
                break
        if slow != -1 and slow == fast:
            return True
    return False


def getIndex(nums, current_index, forward):
    direction = nums[current_index] >= 0
    if forward != direction:
        return -1
    next_index = (current_index+nums[current_index]) % len(nums)
    if next_index == current_index:
        return -1
    return next_index


if __name__ == "__main__":
    nums = [2, -1, 1, 2, 2]
    print(circularArray(nums))
