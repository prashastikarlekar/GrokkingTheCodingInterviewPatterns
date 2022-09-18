# https://leetcode.com/problems/palindrome-linked-list/

# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

# Using extra space


def palindromeI(head):
    if head is None:
        return None
    nums = []
    current = head
    while current:
        nums.append(current.value)
        current = current.next
    return nums == nums[::-1]


# In-place implementation

def palindrome(head):
    if head is None:
        return None
    first_half_end = endOfFirstList(head)
    second_half_start = reverseList(first_half_end.next)

    flag = True
    first = head
    second = second_half_start

    while flag and second:
        if first.value != second.value:
            flag = False
        first = first.next
        second = second.next
    return flag


def endOfFirstList(head):
    if head is None:
        return None
    slow, fast = head, head
    while (fast.next and fast.next.next):  # we want mid as the first of the two middle elements
        slow = slow.next
        fast = fast.next.next
    return slow


def reverseList(head):
    if head is None:
        return None
    previous = None
    current = head
    while current:
        nextNode = current.next
        current.next = previous
        previous = current
        current = nextNode
    return previous


if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(1)
    llist.head.next = Node(2)
    llist.head.next.next = Node(2)
    llist.head.next.next.next = Node(12)
    print(palindrome(llist.head))
