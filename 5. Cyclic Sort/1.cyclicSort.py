# We are given an array containing ‘n’ objects. Each object, when created, was assigned a unique number from 1 to ‘n’ based on their creation sequence. This means that the
# object with sequence number ‘3’ was created just before the object with sequence number ‘4’.
# Write a function to sort the objects in-place on their creation sequence number in O(n)O(n) and without any extra space. For simplicity, let’s assume we are passed an
# integer array containing only the sequence numbers, though each number is actually an object.

def cyclicSort(nums):
    i = 0
    while i < len(nums):
        j = nums[i]-1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    return nums


if __name__ == "__main__":
    nums = [3, 1, 5, 4, 2]
    print(cyclicSort(nums))
