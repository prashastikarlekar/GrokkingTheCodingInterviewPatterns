# https://leetcode.com/problems/minimum-window-substring/

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the
# window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique. A substring is a contiguous sequence of characters within the string.

# Same approach as permutation in string, but here we compare amtches with length of pattern t, and not th elength of hashmap as in permutations one.
# we also match all occurences of characters here.

def minWindow(s, t):
    hashmap = {}
    for i in t:
        if i not in hashmap:
            hashmap[i] = 0
        hashmap[i] += 1
    start, end = 0, 0
    matched = 0
    min_length = float("inf")
    result_start = 0
    while end < len(s):
        if s[end] in hashmap:
            hashmap[s[end]] -= 1
            if hashmap[s[end]] >= 0:
                matched += 1
        print(matched)

        while matched == len(t):
            if min_length > end-start+1:
                min_length = end-start+1
                result_start = start
            leftmost = s[start]
            start += 1
            if leftmost in hashmap:
                if hashmap[leftmost] == 0:
                    matched -= 1
                hashmap[leftmost] += 1
        end += 1
    if min_length > len(s):
        return ""
    return s[result_start:result_start+min_length]


if __name__ == "__main__":
    # s = "ADOBECODEBANC"
    # t = "ABC"
    s = 'aa'
    t = 'aa'
    print(minWindow(s, t))
