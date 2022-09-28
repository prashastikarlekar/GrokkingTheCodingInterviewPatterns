# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

# You are given a string s and an array of strings words. All the strings of words are of the same length. A concatenated substring in s is a substring that contains all the
# strings of any permutation of words concatenated.
# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated
# substring because it is not the concatenation of any permutation of words. Return the starting indices of all the concatenated substrings in s.

def findSubstring(s, words):
    hashmap = {}
    for i in words:
        if i not in hashmap:
            hashmap[i] = 0
        hashmap[i] += 1

    start, end = 0, 0
    result = []
    words_count = len(words)
    words_length = len(words[0])
    for i in range(len(s)-words_count*words_length + 1):
        words_frequency = {}
        for j in range(words_count):
            next_index = i + j*words_length
            word = s[next_index:next_index+words_length]
            if word not in hashmap:
                break
            if word not in words_frequency:
                words_frequency[word] = 0
            words_frequency[word] += 1
            if words_frequency[word] > hashmap.get(word, 0):
                break
            if j+1 == words_count:
                result.append(i)
    return result


if __name__ == "__main__":
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    print(findSubstring(s, words))
