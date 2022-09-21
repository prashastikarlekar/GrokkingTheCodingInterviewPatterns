# https://leetcode.com/problems/longest-repeating-character-replacement/

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation
#  at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.


def longestSubstring(s, k):
    max_length = 0
    start, end = 0, 0
    hashmap = {}
    max_repeating_char = 0
    while end < len(s):
        if s[end] not in hashmap:
            hashmap[s[end]] = 0
        hashmap[s[end]] += 1
        max_repeating_char = max(max_repeating_char, hashmap[s[end]])
        end += 1
        if (end-start-max_repeating_char) > k:
            leftmost = s[start]
            hashmap[leftmost] -= 1
            start += 1
        max_length = max(max_length, end-start)

    return max_length


if __name__ == "__main__":
    s = "ABAB"
    k = 2
    print(longestSubstring(s, k))
