# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string s, find the length of the longest substring without repeating characters.

from collections import defaultdict


def longestSubstring(s):
    max_length = 0
    hashmap = defaultdict()
    start, end = 0, 0
    while end < len(s):
        if s[end] not in hashmap:
            hashmap[s[end]] = end
            end += 1
        else:
            leftmost = min(hashmap.values())
            del hashmap[s[leftmost]]
            start = leftmost+1
        max_length = max(max_length, end-start)
    return max_length


if __name__ == "__main__":
    s = "abcabcbb"
    print(longestSubstring(s))
