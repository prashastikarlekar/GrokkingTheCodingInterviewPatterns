# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should
# remain as it is. You may not alter the values in the list's nodes, only nodes themselves may be changed.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printLL(self):
        while self.head:
            print(self.head.val)
            self.head = self.head.next


def reverseBetween(head, left, right):
    if not head:
        return None
    if left == right:
        return head
    current, prev = head, None
    i = 0
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


def reverseKGroup(head, k):
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    left, right = 1, k
    while right <= length:
        head = reverseBetween(head, left, right)
        left += k
        right += k
    return head


if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(1)
    llist.head.next = Node(2)
    llist.head.next.next = Node(3)
    llist.head.next.next.next = Node(4)
    llist.head.next.next.next.next = Node(5)
    # llist.printLL()
    llist.head = reverseKGroup(llist.head)
    llist.printLL()
