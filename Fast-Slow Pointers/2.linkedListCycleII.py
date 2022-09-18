# https://leetcode.com/problems/linked-list-cycle-ii/

# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally,
# pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not
# passed as a parameter.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        if not self.head:
            return None
        while self.head:
            print(self.head.value)
            head = head.next

# Floyd's Cycle Algorithm


def getIntersect(head):
    slow, fast = head, head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow
    return None


def detectCycle(head):
    if not head:
        return None
    if getIntersect(head) is None:
        return None
    p1, p2 = head, getIntersect(head)
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1

# Using set


def detextCycleII(head):
    if not head:
        return None
    visited = set()
    while head:
        if head in visited:
            return head
        visited.add(head)
        head = head.next

    return None


if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(3)
    llist.head.next = Node(0)
    llist.head.next.next = Node(2)
    llist.head.next.next.next = Node(4)
    llist.head.next.next.next.next = llist.head.next
    print(detectCycle(llist.head))
