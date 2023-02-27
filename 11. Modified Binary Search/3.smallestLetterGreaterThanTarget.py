# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in
# letters. Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first
# character in letters.

def smallestLetterGreaterThan(letters, target):
    start, end = 0, len(letters)-1
    n = len(letters)
    if target > letters[n-1] or target < letters[0]:
        return letters[0]
    while start <= end:
        mid = start + (end-start)//2
        if target < letters[mid]:
            end = mid-1
        else:
            start = mid+1
    return letters[start % n]


if __name__ == "__main__":
    print(smallestLetterGreaterThan(['c', 'f', 'j'], 'z'))
