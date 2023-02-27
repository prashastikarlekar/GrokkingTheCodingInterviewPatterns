# Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’. The ceiling of the ‘key’ will be the smallest element in the
# given array greater than or equal to the ‘key’.

# Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1.

def ceiling(nums, key):
    start, end = 0, len(nums)-1
    if key > nums[end]:
        return -1
    while start <= end:
        mid = start+(end-start)//2
        if key == nums[mid]:
            return mid
        elif key < nums[mid]:
            end = mid-1
        else:
            start = mid+1
    return start


if __name__ == "__main__":
    print(ceiling([1, 3, 8, 10, 15], 7))
