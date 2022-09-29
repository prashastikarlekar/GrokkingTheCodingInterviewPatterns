# https://leetcode.com/problems/reverse-linked-list-ii/

# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return
# the reversed list.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printLL(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

# Implementation #1 - Swapping the values of nodes


def getNodeAt(head, index):
    if not head:
        return None
    current = head
    while (index-1):
        current = current.next
        index -= 1
    return current


def reverseListII(head, left, right):
    if not head:
        return None
    while left < right:
        leftNode = getNodeAt(head, left)
        rightNode = getNodeAt(head, right)
        leftNode.value, rightNode.value = rightNode.value, leftNode.value
        left += 1
        right -= 1
    return head

# Implementation #2 - In-place reversal


def reverseList(head, left, right):
    if not head:
        return None
    if left == right:
        return head
    current, prev, i = head, None, 0
    while current and i < left-1:
        prev = current
        current = current.next
        i += 1
    lastNodeOfFirstPart = prev
    lastNodeOfSecondPart = current
    next, i = None, 0
    while current and i < right-left+1:
        next = current.next
        current.next = prev
        prev = current
        current = next
        i += 1
    if lastNodeOfFirstPart:
        lastNodeOfFirstPart.next = prev
    else:
        head = prev
    lastNodeOfSecondPart.next = current
    return head


if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(1)
    llist.head.next = Node(2)
    llist.head.next.next = Node(3)
    llist.head.next.next.next = Node(4)
    llist.head.next.next.next.next = Node(5)
    # llist.printLL()
    llist.head = reverseList(llist.head, 2, 4)
    llist.printLL()
