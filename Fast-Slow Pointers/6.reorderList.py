# https://leetcode.com/problems/reorder-list/

# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next


def middleOfLinkedList(head):
    if not head:
        return None
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def reorderList(head):
    if head is None:
        return None
    mid = middleOfLinkedList(head)
    current = head
    stack = []
    length = 0
    while current:
        length += 1
        stack.append(Node(current.value))
        current = current.next
    if length < 2:
        return head
    current = head
    while current:
        temp = current.next
        current.next = stack.pop()
        current.next.next = temp if temp != mid else None
        if temp == mid and length % 2 != 0:
            current.next.next = stack.pop()
        current = temp if temp != mid else None

    return head


if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(1)
    llist.head.next = Node(2)
    llist.head.next.next = Node(3)
    llist.head.next.next.next = Node(4)
    llist.head.next.next.next.next = Node(5)
    reorderList(llist.head)
    llist.printList()
