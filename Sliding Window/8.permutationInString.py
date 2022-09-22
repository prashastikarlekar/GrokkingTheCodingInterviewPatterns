# https://leetcode.com/problems/permutation-in-string/

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

def permutation(s1, s2):
    hashmap = {}
    for i in s1:
        if i not in hashmap:
            hashmap[i] = 0
        hashmap[i] += 1

    start, end = 0, 0
    matched = 0
    while end < len(s2):
        if s2[end] in hashmap:
            hashmap[s2[end]] -= 1
            if hashmap[s2[end]] == 0:
                matched += 1
        if matched == len(hashmap):
            return True

        if end-start >= len(s1)-1:
            leftmost = s2[start]
            start += 1
            if leftmost in hashmap:
                if hashmap[leftmost] == 0:
                    matched -= 1
                hashmap[leftmost] += 1
        end += 1
    return False


if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    print(permutation(s1, s2))
