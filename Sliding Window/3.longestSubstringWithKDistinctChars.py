# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

# Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.
from collections import defaultdict


# time limit exceeded, but works for all test cases
def longestSubstringWithKCharsII(s, k):
    max_length = float("-inf")
    for start in range(len(s)):
        end = start
        visited = set()
        while (end-start) <= len(s):
            if s[end] not in visited:
                visited.add(s[end])
            if len(visited) > k:
                break
            max_length = max(max_length, end-start+1)
            if end == len(s)-1:
                break
            else:
                end += 1
    return max_length


def longestSubstringWithKChars(s, k):  # Sliding Window Approach
    max_length = 0
    start, end = 0, 0
    hashmap = defaultdict()    # char - last index of this char in window
    while end < len(s):
        hashmap[s[end]] = end
        end += 1
        if len(hashmap) == k+1:
            leftmost_char_index = min(hashmap.values)
            del hashmap[leftmost_char_index]
            start = leftmost_char_index+1
        max_length = max(max_length, end-start)
    return max_length


if __name__ == "__main__":
    s = 'aaaa'
    k = 1
    print(longestSubstringWithKChars(s, k))
