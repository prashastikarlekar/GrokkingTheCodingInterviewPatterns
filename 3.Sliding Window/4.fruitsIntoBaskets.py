# https://leetcode.com/problems/fruit-into-baskets/

# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type
# of fruit the ith tree produces. You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.

from collections import defaultdict


def totalFruit(fruits):
    max_fruits = 0
    start, end = 0, 0
    hashmap = defaultdict()
    while end < len(fruits):
        hashmap[fruits[end]] = end
        end += 1
        if len(hashmap) == 3:
            leftmost = min(hashmap.values())
            del hashmap[fruits[leftmost]]
            start = leftmost+1
        max_fruits = max(max_fruits, end-start)
    return max_fruits


if __name__ == "__main__":
    fruits = [1, 2, 1]
    print(totalFruit(fruits))
