# https://leetcode.com/problems/letter-case-permutation/

# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
# Return a list of all possible strings we could create. Return the output in any order.
from collections import deque


def letterCasePermutation(s):
    result = []
    permutation = deque()
    permutation.append([])
    sLength = len(s)
    for current in s:
        n = len(permutation)
        for _ in range(len(permutation)):
            oldPermutation = permutation.popleft()
            newPermutation = list(oldPermutation)
            newPermutation.append(current)
            if current.isalpha():
                capitalPermutation = list(oldPermutation)
                if current.isupper():
                    capitalPermutation.append(current.lower())
                else:
                    capitalPermutation.append(current.upper())
            if len(newPermutation) == sLength:

                result.append(("".join([x for x in newPermutation])))
            else:
                permutation.append(newPermutation)
            if len(capitalPermutation) == sLength:
                result.append(("".join([x for x in capitalPermutation])))
            else:
                permutation.append(capitalPermutation)
    return result


if __name__ == "__main__":
    s = 'a1b2'
    print(letterCasePermutation(s))
