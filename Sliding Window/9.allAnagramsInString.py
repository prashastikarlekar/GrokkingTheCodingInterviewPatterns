# https://leetcode.com/problems/find-all-anagrams-in-a-string/

# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def findAnagrams(s, p):
    hashmap = {}
    result = []
    for i in p:
        if i not in hashmap:
            hashmap[i] = 0
        hashmap[i] += 1
    start, end = 0, 0
    matched = 0
    while end < len(s):
        if s[end] in hashmap:
            hashmap[s[end]] -= 1
            if hashmap[s[end]] == 0:
                matched += 1

        if matched == len(hashmap):
            result.append([start, end])
            # matched = 0

        if end-start >= len(p)-1:
            leftmost = s[start]
            start += 1
            if leftmost in hashmap:
                if hashmap[leftmost] == 0:
                    matched -= 1
                hashmap[leftmost] += 1
        end += 1
    return result


if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    print(findAnagrams(s, p))
