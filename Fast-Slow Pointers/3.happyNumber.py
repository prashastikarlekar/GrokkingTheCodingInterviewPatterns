# https://leetcode.com/problems/happy-number/

# Write an algorithm to determine if a number n is happy. A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

def happyNumber(n):

    def getSum(n):
        sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            sum += digit**2
        return sum

    slow = n
    fast = getSum(n)
    while slow != fast and fast != 1:
        slow = getSum(slow)
        fast = getSum(getSum(fast))
    return fast == 1

# Using Set
    # visited=set()
    # while n!=1 and n not in visited:
    #     visited.add(n)
    #     n=getSum(n)
    # return n==1


if __name__ == "__main__":
    print(happyNumber(10))
