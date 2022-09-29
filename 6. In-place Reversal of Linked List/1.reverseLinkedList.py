# https://leetcode.com/problems/reverse-linked-list/

# Given the head of a singly linked list, reverse the list, and return the reversed list.

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


def reverseList(head):
    if not head:
        return None
    prev, current, next = None, head, None
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev


if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(1)
    llist.head.next = Node(2)
    llist.head.next.next = Node(3)
    llist.head.next.next.next = Node(4)
    llist.head.next.next.next.next = Node(5)
    # llist.printLL()
    llist.head = reverseList(llist.head)
    llist.printLL()
