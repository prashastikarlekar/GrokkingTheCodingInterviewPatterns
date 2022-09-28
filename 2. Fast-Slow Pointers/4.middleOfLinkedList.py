# https://leetcode.com/problems/middle-of-the-linked-list/

# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


def middleOfList(head):
    if not head:
        return None
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(1)
    llist.head.next = Node(2)
    llist.head.next.next = Node(3)
    llist.head.next.next.next = Node(4)
    llist.head.next.next.next.next = Node(5)
    print(middleOfList(llist.head))
